from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.autoreplybot.models import AgorabitWhoMSg
from app.autoreplybot.models import Base
#
#
# def add_user(datestamp, subreddit, username):
#     addtheuser = AgorabitWhoMSg(datestamp=datestamp, subreddit=subreddit, username=username)
#     session.add(addtheuser)
#     session.commit()
#
