from decimal import Decimal
from django.http.response import Http404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.db.models import Count, Sum
from .models import Match
from .forms import MakeABetForm

class MakeABetView(View):
    form_class = MakeABetForm
    initial = {'amount': Decimal(10)}
    template_name = 'pool/make_a_bet.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("pool:thank-you"))

        return render(request, self.template_name, {'form': form})


class PlacedBetsView(View):
    template_name = "pool/placed_bets.html"

    def get(self, request, *args, **kwargs):
        matches = Match.objects.all().annotate(num_bets=Count('bet')).order_by('plays_at')
        return render(request, self.template_name, {'matches': matches})


class PlacedBetsPerMatchView(View):
    template_name = "pool/placed_bets_per_match.html"

    def get(self, request, match_id: int, *args, **kwargs):

        try:
            match = Match.objects.get(pk=match_id)
        except Match.DoesNotExist:
            raise Http404("Match does not exist")

        bets = match.bet_set.all().order_by('-added')
        amount_sum = match.bet_set.aggregate(Sum('amount'))['amount__sum']

        return render(request, self.template_name, {'match': match,
                                                    'bets': bets, 'amount_sum': amount_sum})

