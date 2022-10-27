from django.template import defaultfilters
from django.forms.models import ModelChoiceField
from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput
from pool.models import Bet, Match
from decimal import Decimal


class MatchChoiceField(ModelChoiceField):
    def label_from_instance(self, match):
        return "{d} {m1} - {m2}".format(d=defaultfilters.date(match.plays_at, "d N Y"),
                                        m1=match.team_1, m2=match.team_2)


class MakeABetForm(ModelForm):
    """
    Form to insert a bet
    """

    the_match = MatchChoiceField(queryset=Match.objects.all().order_by('plays_at'))

    class Meta:
        model = Bet
        fields = ["person_name", "the_match", "team_1_points", "team_2_points", "amount"]
        widgets = {
            'person_name': TextInput(attrs={'placeholder': "Your name"}),
        }

    def clean_amount(self) -> Decimal:
        data = self.cleaned_data['amount']
        if data <= Decimal(0):
            raise ValidationError("At least EUR 1", code="too_less")
        if data > Decimal(100):
            raise ValidationError("The maximum is EUR 100", code="too_much")

        return data
