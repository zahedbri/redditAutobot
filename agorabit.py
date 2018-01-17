from database_stuff import add_user
from datetime import datetime
import praw
from models import Users
from database_stuff import session
now = datetime.utcnow()


reddit = praw.Reddit(client_id='rqlqlTdlJA5r8g',
                     client_secret='mZq_vwnY_Li5oKMYD9bL0FaU9ys',
                     password='ilovecorn1234',
                     user_agent='correlates data',
                     username='bloatedgut4354')

thesubs = ['python']


# agorabit messaging
the_message = 'Hey, you should try agorabit.com.  Its got 0 fees, has btc cash, and doesnt rip you off' \
              'with wallet fees.  Easier to use too than localbitcoins.'
subject = 'hey man'
#

modlist = []

def new_getusersub():

    for sub in thesubs:
        subreddit = reddit.subreddit(sub)
        hot = subreddit.hot(limit=5)

        for moderator in reddit.subreddit(sub).moderator():
            modlist.append(moderator)

        for submission in hot:
            if not submission.stickied:
                printheader(submission=submission)
                printcomments(submission, sub=sub)




def printheader(submission):
    print('')
    print(20 * '#')
    print('Title: {},'
          ' ups: {},'
          ' downs: {},'
          ' subid: {}'.format(submission.title,
                              submission.ups,
                              submission.downs,
                              submission.id))
    print(20 * '#')
    print('')
    print('')
    print('')


def printcomments(submission, sub):
    comments = submission.comments
    for comment in comments:
        print(10 * '**')
        print('Author:', comment.author)
        print('Parent ID:', comment.parent())
        print('Comment ID:', comment.id)

        getcomments(comment=comment, sub=sub)

def getcomments(comment, sub):
    for f in comment.replies:
        print('REPLY:')
        print(f.author)
        #dothework(f, sub=sub)




def dothework(f, sub):
    if f.author in modlist:
        pass
    else:
        add_user(datestamp=now, subreddit=str(sub), username=str(f.author))
        send_msg(reddituser=f.author, msg=the_message, thesubject=subject)


def send_msg(reddituser, msg, thesubject):
    reddit.redditor(reddituser).message(thesubject, msg)





new_getusersub()


