from ..models import User,Session
import uuid
from datetime import datetime, timedelta

SALT = "51d2ca33-3c40-4c4f-b3b5-b370e5c6d87a"

def get_new_uid():
    return uuid.uuid4()

def salt_and_hash(passw):
    return passw

def do_login(login, passw):
    try:
        user = User.objects.get(username=login)
    except User.DoesNotExist:
        return None
    hashed_pass = salt_and_hash(passw)
    if user.password != hashed_pass:
        return None

    session = Session()
    session.key = get_new_uid()
    session.user = user
    session.expires = datetime.now() + timedelta(hours=6)
    session.save()

    return session.key

