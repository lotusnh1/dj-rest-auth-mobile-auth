from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
from . models import Otp
from django.conf import settings


User=get_user_model()

class MobileAuthentication(BaseBackend):
    """
    Authenticate with Phone Number

    """

    def _delete_otp_(self,phonenumber):

        Otp.objects.filter(phonenumber=phonenumber).delete()


    def authenticate(self, request, phonenumber=None):
     
       
        try:
          
            user = User.objects.get(phonenumber=phonenumber)
        except User.DoesNotExist:
         
           
            user = User(phonenumber=phonenumber)
            user.is_staff = False
            user.is_superuser = False
            user.save()

        if settings.DRA_DELETE_OTP_AFTER_LOGIN:

            self._delete_otp_(phonenumber)

    
        return user
       

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None