from app import session2
from app.torbot.models import TorBots


new_person = TorBots(username='new person')
session2.add(new_person)
session2.commit()

