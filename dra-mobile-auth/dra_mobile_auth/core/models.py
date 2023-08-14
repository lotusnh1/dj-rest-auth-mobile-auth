from django.db import models
from datetime import  timedelta
import pytz
from datetime import datetime
from django.conf import settings


class Otp(models.Model):
    phonenumber=models.CharField(max_length=200)
    code=models.IntegerField()
    expiration_date = models.DateTimeField(blank=True,null=True)


    def __str__(self):
        return str(self.code)



    
    def save(self,*args,**kwargs):

        minutes_to_add=2

        if  hasattr(settings, 'DRA_OTP_EXPIRATION'):

            minutes_to_add = settings.DRA_OTP_EXPIRATION
      

        now = datetime.now(pytz.timezone(settings.TIME_ZONE))     
        self.expiration_date= now + timedelta(minutes=minutes_to_add)
      
        super(Otp,self).save(*args, **kwargs)
