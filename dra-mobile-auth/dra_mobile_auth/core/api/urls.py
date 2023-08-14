from django.urls import path
from .views import OneTimePasswordAuthenticationView


urlpatterns = [
  
    path('otp', OneTimePasswordAuthenticationView.as_view(), name='send-mobile'),
   

   

]