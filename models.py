from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Users(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    datestamp = Column(String(255))
    subreddit = Column(String(255))
    username = Column(String(255))

class subs(Base):
    __tablename__ = "Subs"
    id = Column(Integer, primary_key=True)
    datestamp = Column(String(255))
    Parent_ID = Column(String(255))
