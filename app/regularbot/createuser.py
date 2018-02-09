from app import session2
from app.regularbot.models import Bots



new_person = Bots(username='rundsafdsas',
                     password='redditmanredditman',
                     appname='dssadfdshgjj',
                     clientid='q8oX8unzP9EjfA',
                     clientsecret='1y7e4V2jV8Nt5AmF5umHy01t9js',
                     useragent='dsafsadf',
                     )
session2.add(new_person)
session2.commit()
