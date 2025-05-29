from django.urls import path
from . import views

urlpatterns = [
    path('enter-patient/', views.enter_patient, name='enter_patient'),
    path('thank-you/', views.thank_you, name='thank_you'),
]
