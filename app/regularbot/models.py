from sqlalchemy import Column, Integer, String
from app import Base
from app import engine


class Bots(Base):
    __tablename__ = "users"
    __bind_key__ = 'redditbot'
    __table_args__ = {'useexisting': True}
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255))
    password = Column(String(255))
    appname = Column(String(255))
    clientid = Column(String(255))
    clientsecret = Column(String(255))
    useragent = Column(String(255))


class AgorabitWhoMSg(Base):
    __tablename__ = "who_agorabit"
    __bind_key__ = 'redditbot'
    __table_args__ = {'useexisting': True}
    id = Column(Integer, primary_key=True)
    datestamp = Column(String(255))
    subreddit = Column(String(255))
    username = Column(String(255))


class Subs(Base):
    __tablename__ = "subs"
    __bind_key__ = 'redditbot'
    __table_args__ = {'useexisting': True}
    id = Column(Integer, primary_key=True)
    datestamp = Column(String(255))
    Parent_ID = Column(String(255))


Base.metadata.create_all(engine)
