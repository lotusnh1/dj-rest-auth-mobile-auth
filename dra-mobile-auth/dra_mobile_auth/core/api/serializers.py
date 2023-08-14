from rest_framework import serializers
from dj_rest_auth.serializers import LoginSerializer
from rest_framework.exceptions import APIException
import phonenumbers
from ..models import Otp
from datetime import datetime
import time
import pytz
from django.conf import settings





class PhoneNumberNotValid(APIException):
    status_code = 400
    default_detail = 'Phonenumber is not a valid Number!'
    default_code = 'phonenumber_not_valid'


class OtpNotValid(APIException):
    status_code = 401
    default_detail = 'Otp is invalid or expired!'
    default_code = 'otp_not_valid'


class CredentialsNotValid(APIException):
    status_code = 401
    default_detail = 'Unable to log in with provided credentials'
    default_code = 'credentials_not_valid'



class OneTimePasswordSerilizer(serializers.Serializer):

    phonenumber = serializers.CharField()

    def validate(self, data):
     
        

        try :
             
                if phonenumbers.is_valid_number(phonenumbers.parse(data['phonenumber'], None)):

                        return data
                else :
                        raise PhoneNumberNotValid
        except :

                raise PhoneNumberNotValid
        



class CustomLoginSerializer(LoginSerializer):
        activation_code = serializers.IntegerField()
        phonenumber = serializers.CharField()
        username = serializers.CharField(required=False, allow_blank=True)
        email = serializers.EmailField(required=False, allow_blank=True)
        password = serializers.CharField(required=False,allow_blank=True,style={'input_type': 'password'})

        def _validate_otp_code(self,otp,phonenumber):
                
                try :

                        code = Otp.objects.get(phonenumber=phonenumber,code=otp)
                        now = datetime.now(pytz.timezone(settings.TIME_ZONE))
                        if now > code.expiration_date :
                                return False

                        return True
                                
                except Otp.DoesNotExist:

                        return False

    

        def validate(self, data):

        
                validation = self._validate_otp_code(data['activation_code'],data['phonenumber'])
                if validation :
                        user = self.authenticate(phonenumber=data['phonenumber'])
                        if not user:

                                raise CredentialsNotValid

                        data['user']=user
                        return data

                raise OtpNotValid