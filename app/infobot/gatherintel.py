from app import session2
from app.infobot.models import FunnyStuff, FoodStuff
import praw

subs = ['funny', 'food', 'pizza', 'sushi']

banstuff = ['**', 'http', '**', '/r', 'r/', '/R', 'removed', '[removed]', 'ban', '[deleted]', 'fuck', "FUCK", 'Fuck']


def addComment(sub, comment):

    try:
        if sub == 'funny' or sub == 'pizza' or sub == 'sushi':
            addcomment = FunnyStuff(comment=comment)
            session2.add(addcomment)
            session2.commit()

        elif sub == 'food':

            addcommentfood = FoodStuff(comment=comment)
            session2.add(addcommentfood)
            session2.commit()

        else:
            pass
    except Exception as e:
        session2.rollback()
        pass


def main():

    username = 'redbeerdawg12'
    reddit = praw.Reddit(client_id='vJYSY6c--NRTTQ',
                         client_secret='x2JaRHC4HgzgiYmaCHMRioBrO-o',
                         password='richardnixon1975',
                         user_agent='crawling every day',
                         username=username)
    for sub in subs:



        subreddit = reddit.subreddit(sub)
        submissions = subreddit.hot(limit=100)

        for submission in submissions:
            try:
                for comment in submission.comments:
                    if len(comment.body) <= 50:
                        if comment.body in banstuff:
                            pass
                        else:
                            x = comment.body
                            addComment(sub=sub,
                                       comment=x)



            except Exception as e:
                pass


main()