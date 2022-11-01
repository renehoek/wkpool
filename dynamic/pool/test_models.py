from django.test import TestCase
import datetime
from decimal import Decimal
from django.utils import timezone
from pool.models import Match, Team, Bet


class ModelTestCase(TestCase):
    def test_should_store_model(self):
        # Create and store two teams
        my_team_red = Team(name="Team red")
        my_team_red.save()

        my_team_blue = Team(name="Team blue")
        my_team_blue.save()

        # Create a match, link the two teams and store it.
        my_match = Match()
        my_match.plays_at = timezone.make_aware(datetime.datetime(2022, 12, 18))
        my_match.team_1 = my_team_red
        my_match.team_2 = my_team_blue
        my_match.stadion = "AL_THUMAMA"
        my_match.save()

        matches = Match.objects.filter(stadion="AL_THUMAMA")
        self.assertListEqual(list(matches), [my_match])
        print(matches)

    def test_sum_amount_of_bets(self):
        # Create and store two teams
        my_team_red = Team(name="Team red")
        my_team_red.save()

        my_team_blue = Team(name="Team blue")
        my_team_blue.save()

        # Create a match
        my_match = Match(plays_at=timezone.make_aware(datetime.datetime(2022, 12, 18)),
                         team_1=my_team_red, team_2=my_team_blue, stadion="AL_THUMAMA")
        my_match.save()

        # Create two bets
        bet_1 = Bet(person_name="Rene", the_match=my_match, team_1_points=2, team_2_points=3, amount=Decimal(7))
        bet_1.save()
        bet_2 = Bet(person_name="Rene", the_match=my_match, team_1_points=2, team_2_points=3, amount=Decimal(15))
        bet_2.save()

        self.assertEqual(my_match.bet_set.sum_of_bets(), Decimal(22))
        print("Bet first: {d}".format(d=my_match.bet_set.sum_of_bets()))

        # Increase a bet
        bet_2.amount = 20
        bet_2.save()

        self.assertEqual(my_match.bet_set.sum_of_bets(), Decimal(27))
        print("Bet second: {d}".format(d=my_match.bet_set.sum_of_bets()))
