from django.urls import path
from .views import redeem_ticket, home, generate_ticket

urlpatterns = [
    path('', home), 
    path('redeem/<uuid:code>/', redeem_ticket),
    path('generate/', generate_ticket),
]