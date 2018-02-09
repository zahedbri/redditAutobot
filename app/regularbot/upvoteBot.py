from datetime import datetime
import praw
from app.regularbot.models import Bots
from app import session
from sqlalchemy import func
import time
now = datetime.utcnow()

def main(number, submissionid):
    theuser = session.query(Bots).filter(Bots.id <= 10).order_by(func.rand()).limit(number)
    for user in theuser:
        print("*"*10)
        print("User: ", user.username)
        reddit = praw.Reddit(client_id=user.clientid,
                             client_secret=user.clientsecret,
                             password=user.password,
                             user_agent=user.useragent,
                             username=user.username)


        x = reddit.submission(id=submissionid)
        print(x)
        print(x.title)
        print("*" * 10)
        #time.sleep(100)



