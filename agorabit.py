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

thesubs = ['localbitcoins']


# agorabit messaging
the_message = 'Hey, you should try agorabit.com.' \
              '  Its got 0 fees, doesnt lock you out,' \
              ' has btc cash, and doesnt rip you off' \
              'with wallet fees.  Easier to use too than localbitcoins.'
subject = 'hey man'
#

modlist = []
getwork = 1
verbose = 1

def sendauthormsg(submission, sub):
    if verbose == 1:
        print('Author: ', submission.author)

    if getwork == 1:
        dothework_noloop(f=submission, sub=sub)


def printheader(submission, sub):
    if verbose == 1:
        print('')
        print(20 * '#')
        print('sub:', sub)
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

    for f in comments:
        if verbose == 1:
            print(10 * '**')
            print('Author:', f.author)
            print('Parent ID:', f.parent())
            print('Comment ID:', f.id)

        if getwork == 1:
            dothework(f, sub=sub)
            getcomments(comment=f, sub=sub)


def getcomments(comment, sub):

        for f in comment.replies:
            if verbose == 1:
                print('REPLY:')
                print(f.author)

            if getwork == 1:
                dothework(f, sub=sub)


def dothework_noloop(f, sub):
    if verbose == 1:
        if f.author in modlist:
            print(20 * '!')
            print(f.author)
            print(20 * '!')
    if getwork == 1:
        seeifuser = session.query(Users).filter_by(username=str(f.author)).first()
        if seeifuser is None:
            print("no user..proceeding to add")
            add_user(datestamp=str(now), subreddit=str(sub), username=str(f.author))
            send_msg(reddituser=f.author, msg=the_message, thesubject=subject)
        else:
            print("Exists. Not adding to db:", seeifuser.username)
            pass


def dothework(f, sub):
    if f.author in modlist:
        if verbose == 1:
            print(20 * '!')
            print(f.author)
            print(20 * '!')
    if getwork == 1:
        seeifuser = session.query(Users).filter_by(username=str(f.author)).first()
        if seeifuser is None:
            print("no user..proceeding to add")
            add_user(datestamp=str(now), subreddit=str(sub), username=str(f.author))
            send_msg(reddituser=f.author, msg=the_message, thesubject=subject)
        else:
            print("Exists. Not adding to db:", seeifuser.username)
            pass


def send_msg(reddituser, msg, thesubject):
    struser = str(reddituser)
    strmsg = str(msg)
    strsubj = (str(thesubject))

    reddit.redditor(struser).message(strsubj, strmsg)
    if verbose == 1:
        print("Sent messge:", struser)


def main():
    for sub in thesubs:
        subreddit = reddit.subreddit(sub)
        hot = subreddit.hot(limit=1)

        for moderator in reddit.subreddit(sub).moderator():
            modlist.append(moderator)

        for submission in hot:
            if not submission.stickied:
                printheader(submission=submission, sub=sub)
                sendauthormsg(submission=submission, sub=sub)
                printcomments(submission=submission, sub=sub)


main()


