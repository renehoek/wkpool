from django.contrib import admin
from .models import Bet, Match, Team

@admin.register(Bet)
class PouleAdmin(admin.ModelAdmin):
    pass

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    pass

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass
