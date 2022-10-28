from decimal import Decimal
from typing import Optional
from django.http.request import HttpRequest
from django.http.response import Http404, HttpResponse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.db.models import Count
from .models import Match, Bet
from .forms import MakeABetForm


class ManageABetView(View):
    form_class = MakeABetForm
    initial = {}
    instance = None
    template_name = 'pool/make_a_bet.html'
    success_url = reverse_lazy("pool:thank-you")

    def get_initial(self) -> dict:
        return self.initial.copy()

    def get_instance(self) -> Optional[Bet]:
        return self.instance

    def get_form_kwargs(self) -> dict:
        kwargs = {"initial": self.get_initial()}
        if self.request.method in ("POST", "PUT"):
            kwargs.update({"data": self.request.POST, "files": self.request.FILES})
        if self.instance is not None:
            kwargs.update({"instance": self.get_instance()})
        return kwargs

    def handle_post(self, request: HttpRequest) -> HttpResponse:
        form = self.form_class(**self.get_form_kwargs())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)

        return render(request, self.template_name, {'form': form})


class AddABetView(ManageABetView):
    initial = {'amount': Decimal(10)}

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = self.form_class(**self.get_form_kwargs())
        return render(request, self.template_name, {'form': form})

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return self.handle_post(request)


class UpdateABetView(ManageABetView):

    def _get_the_bet(self, bet_id: int) -> Bet:
        try:
            return Bet.objects.get(pk=bet_id)
        except Bet.DoesNotExist:
            raise Http404("Bet Does not exist")

    def get(self, request: HttpRequest, bet_id: int, *args, **kwargs) -> HttpResponse:
        self.instance = self._get_the_bet(bet_id)
        form = self.form_class(**self.get_form_kwargs())
        return render(request, self.template_name, {'form': form})

    def post(self, request: HttpRequest, bet_id: int, *args, **kwargs) -> HttpResponse:
        self.instance = self._get_the_bet(bet_id)
        return self.handle_post(request)


class PlacedBetsView(View):
    template_name = "pool/placed_bets.html"

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        matches = Match.objects.all().annotate(num_bets=Count('bet')).order_by('plays_at')
        return render(request, self.template_name, {'matches': matches})


class PlacedBetsPerMatchView(View):
    template_name = "pool/placed_bets_per_match.html"

    def get(self, request: HttpRequest, match_id: int, *args, **kwargs) -> HttpResponse:

        try:
            match = Match.objects.get(pk=match_id)
        except Match.DoesNotExist:
            raise Http404("Match does not exist")

        bets = match.bet_set.all().order_by('-added')
        amount_sum = match.bet_set.sum_of_bets()

        return render(request, self.template_name, {'match': match,
                                                    'bets': bets, 'amount_sum': amount_sum})
