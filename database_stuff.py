
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Users


db = create_engine('sqlite:////home/droid/gitbox/redditAutobot/database.db')
db.echo = False  # Try changing this to True and see what happens
connection = db.connect()
Session = sessionmaker(bind=db)
session = Session()
Base = declarative_base()

def add_user(datestamp, subreddit, username):
    addtheuser = Users(datestamp=datestamp, subreddit=subreddit, username=username)
    session.add(addtheuser)
    session.commit()

