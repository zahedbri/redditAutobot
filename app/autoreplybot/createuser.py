from app import session
from app.autoreplybot.models import TorBots


new_person = TorBots(username='new person')
session.add(new_person)
session.commit()

