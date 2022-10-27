from django.db import models

class Team(models.Model):
    """
    The football team playing
    """
    name = models.CharField(blank=False, max_length=255)

    class Meta:
        verbose_name = "Team"

    def __str__(self):
        return self.name


class Match(models.Model):
    """
    The match between two teams.
    """

    STADION_CHOICES = (('AL_BAYT', 'Al Bayt'), ('KHALIFA_INT', 'Khalifa Int'),
                       ('AHMAD_BIN_ALI', 'Ahmad Bin Ali'), ('AL_THUMAMA', 'Al Thumama'))

    plays_at = models.DateTimeField(blank=False)
    team_1 = models.ForeignKey(Team, blank=False, related_name="match_team_1", on_delete=models.PROTECT)
    team_2 = models.ForeignKey(Team, blank=False, related_name="match_team_2", on_delete=models.PROTECT)
    stadion = models.CharField(choices=STADION_CHOICES, max_length=255)

    class Meta:
        verbose_name = "The match"
        verbose_name_plural = "The matches"

    def __str__(self):
        return "{dt} {t1} - {t2}".format(dt=self.plays_at, t1=self.team_1, t2=self.team_2)


class Bet(models.Model):
    """
    A placed bet for a match
    """
    added = models.DateTimeField(auto_now_add=True)
    person_name = models.CharField(blank=False, max_length=255)
    the_match = models.ForeignKey(Match, on_delete=models.PROTECT)
    team_1_points = models.PositiveIntegerField()
    team_2_points = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=3, decimal_places=0)

    class Meta:
        verbose_name = "Bet"

    def __str__(self):
        return "{p} - {m}: {t1}/{t2}".format(p=self.person_name, m=self.the_match,
                                             t1=self.team_1_points, t2=self.team_2_points)
