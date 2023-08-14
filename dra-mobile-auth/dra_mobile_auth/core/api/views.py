
from rest_framework.permissions import IsAuthenticated ,AllowAny
from dj_rest_auth.views import LoginView
from rest_framework.views import APIView
from .serializers import OneTimePasswordSerilizer
from ..models import Otp
import random
from rest_framework.response import Response
from rest_framework import status
from .throttles import HourRateThrottle,DayRateThrottle,MinuteRateThrottle
from django.conf import settings

Throttle=[]

if  settings.THROTTLE:
    Throttle=[MinuteRateThrottle,HourRateThrottle,DayRateThrottle]







class OneTimePasswordAuthenticationView(APIView):
    permission_classes = [AllowAny]
    throttle_classes = Throttle

    

    def generate_one_time_password(self):
        '''
          Create a number to send to user in sms to login or register
        '''

       
        OTP = ""

        for i in range(6) :
            OTP=OTP+str(random.choice(range(0,9)))

        return OTP

    def save_otp(self,otp,phonenumber):
        try :

            Otp.objects.create(phonenumber=phonenumber,code=otp)
            return True

        except :
            return False
        


        

    def post(self, request):

        serializer = OneTimePasswordSerilizer(data=request.data)  
       
        if serializer.is_valid():
            one_time_password=self.generate_one_time_password()
    
            if self.save_otp(one_time_password,serializer.data['phonenumber']):
          
  
                return Response({'message':"Ok !"},status=status.HTTP_200_OK)
          
            return Response({'message':"otp  was not created!"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response({'message':"bad data !"},status=status.HTTP_400_BAD_REQUEST)









