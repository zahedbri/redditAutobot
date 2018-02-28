from datetime import datetime
import praw
from app.regularbot.models import Bots
from app import session
from sqlalchemy import func

now = datetime.utcnow()


def main(submissionid, msg):
    theuser = session.query(Bots).filter(Bots.id).order_by(func.rand()).limit(1)
    for user in theuser:
        print("*"*10)
        print("User: ", user.username)
        reddit = praw.Reddit(client_id=user.clientid,
                             client_secret=user.clientsecret,
                             password=user.password,
                             user_agent=user.useragent,
                             username=user.username)

        x = reddit.submission(id=submissionid)
        x.reply(msg)
        print(x)
        print(x.title)
        print(x.url)
        print("MSG: ", msg)
        print("*" * 10)





