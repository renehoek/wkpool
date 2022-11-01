from django.views.generic.base import TemplateView, RedirectView
from django.urls import path, include
from . import views

pool_patterns = ([
     path('', TemplateView.as_view(template_name="pool/home.html"), name="home"),
     path('make-a-bet/', views.AddABetView.as_view(), name="make-bet"),
     path('make-a-bet/thank-you/', TemplateView.as_view(template_name="pool/bet_placed.html"), name="thank-you"),
     path('update-a-bet/<int:bet_id>/', views.UpdateABetView.as_view(), name="update-bet"),
     path('update-a-bet/thank-you/', TemplateView.as_view(template_name="pool/bet_placed.html"), name="thank-you-update"),
     path('placed-bets/overview/', views.PlacedBetsView.as_view(), name="bets-overview"),
     path('placed-bets/<int:match_id>/', views.PlacedBetsPerMatchView.as_view(), name="bets-per-match"),

     path('sheets/sheet-1/', TemplateView.as_view(template_name="pool/sheets/sheet_1.html"), name="sheet-1"),
     path('sheets/sheet-2/', TemplateView.as_view(template_name="pool/sheets/sheet_2.html"), name="sheet-2"),
     path('sheets/sheet-3/', TemplateView.as_view(template_name="pool/sheets/sheet_3.html"), name="sheet-3"),
     path('sheets/sheet-4/', TemplateView.as_view(template_name="pool/sheets/sheet_4.html"), name="sheet-4"),
     path('sheets/sheet-5/', TemplateView.as_view(template_name="pool/sheets/sheet_5.html"), name="sheet-5"),
     path('sheets/sheet-6/', TemplateView.as_view(template_name="pool/sheets/sheet_6.html"), name="sheet-6"),
     path('sheets/sheet-7/', TemplateView.as_view(template_name="pool/sheets/sheet_7.html"), name="sheet-7"),
     path('sheets/sheet-8/', TemplateView.as_view(template_name="pool/sheets/sheet_8.html"), name="sheet-8"),

 ], 'pool')

urlpatterns = [path('', include(pool_patterns))]
