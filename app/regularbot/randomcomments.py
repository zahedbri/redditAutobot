from datetime import datetime
import praw
from app.regularbot.models import Bots
from app.infobot.models import FunnyStuff, FoodStuff
from app import session, session2
from sqlalchemy import func
import random
import time

now = datetime.utcnow()


subs = ['funny', 'food', 'pizza', 'sushi']

def addComment(sub, post):

        if sub == 'food' or sub == 'pizza' or sub == 'sushi':
            getquote = session2.query(FoodStuff).order_by(func.rand()).first()

            print("sub", sub)
            try:
                post.reply(str(getquote.comment))
            except:
                pass
            print("getquote.comment")
            print("added comment ..")
        elif sub == 'funny':
            getquote = session2.query(FunnyStuff).order_by(func.rand()).first()

            print(getquote.id)
            try:
                post.reply(str(getquote.comment))
            except:
                pass
            print("getquote.comment")
            print("added comment ..")
        else:
            print("failue")
            pass


def main():
    user = session.query(Bots).order_by(func.rand()).first()
    print("*" * 10)
    print("User: ", user.username)
    reddit = praw.Reddit(client_id=user.clientid,
                         client_secret=user.clientsecret,
                         password=user.password,
                         user_agent=user.useragent,
                         username=user.username)

    subz = random.choice(subs)
    submissions = reddit.subreddit(subz).hot(limit=5)

    for s in submissions:
        if s.stickied:
            continue
        else:

            print(s.title)
            addComment(post=s, sub=subz)
            time.sleep(500)





