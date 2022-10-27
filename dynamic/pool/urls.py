from django.views.generic.base import TemplateView, RedirectView
from django.urls import path, include
from . import views

pool_patterns = ([
         path('', RedirectView.as_view(pattern_name='pool:make-bet'), name="home"),
         path('make-a-bet/', views.MakeABetView.as_view(), name="make-bet"),
         path('make-a-bet/thank-you/', TemplateView.as_view(template_name="pool/bet_placed.html"), name="thank-you"),
         path('placed-bets/overview/', views.PlacedBetsView.as_view(), name="bets-overview"),
         path('placed-bets/<int:match_id>/', views.PlacedBetsPerMatchView.as_view(), name="bets-per-match"),
     ], 'pool')

urlpatterns = [path('', include(pool_patterns))]
