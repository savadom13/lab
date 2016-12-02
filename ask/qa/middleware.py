from .models import Session
from datetime import datetime
# from django.http import request

debug = True

class CheckSessionMiddleware(object):
    def process_request(self, request):
        # return None
         try:
             sessionid = request.COOKIES.get('sessionid')
             session = Session.objects.get(
                 key=sessionid,
                 expires__gt=datetime.now(),
             )
             if debug: print "user = " + str(session.user)
             request.session = session
             request.user = session.user
         except Session.DoesNotExist:
             request.session = None
             request.user = None
             if debug: print "user = Anonimus"