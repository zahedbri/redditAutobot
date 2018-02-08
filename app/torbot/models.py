from sqlalchemy import Column, Integer, String
from app import Base2
from app import engine2

class TorBots(Base2):
    __tablename__ = "users"
    __bind_key__ = 'torbot'
    __table_args__ = {'useexisting': True}
    id = Column(Integer, primary_key=True)
    username = Column(String(255))
    # password = Column(String(255))
    # appname = Column(String(255))
    # clientid = Column(String(255))
    # clientsecret = Column(String(255))
    # useragent = Column(String(255))
    #



Base2.metadata.create_all(engine2)
