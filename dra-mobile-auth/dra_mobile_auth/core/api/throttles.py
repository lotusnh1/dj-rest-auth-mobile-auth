from rest_framework.throttling import AnonRateThrottle
from rest_framework.views import exception_handler
from rest_framework.exceptions import Throttled



class MinuteRateThrottle(AnonRateThrottle):

    scope = 'dra_minute'

class HourRateThrottle(AnonRateThrottle):

    scope = 'dra_hour'

class DayRateThrottle(AnonRateThrottle):

    scope = 'dra_day'









def custom_exception_handler(exc, context):
  
    response = exception_handler(exc, context)


    if isinstance(exc, Throttled):
       
        
        custom_response_data = { 
            'message': 'request limit exceeded',
            'availableIn': exc.wait,
            
        }
        response.data = custom_response_data 
    return response
