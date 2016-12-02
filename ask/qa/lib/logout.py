from ..models import Session

def do_logout(sessionid):
    try:
        session = Session.objects.get(key=sessionid)
        session.delete()
    except:
        pass