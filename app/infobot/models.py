from sqlalchemy import Column, Integer, String
from app import Base2
from app import engine2


class FunnyStuff(Base2):
    __tablename__ = "funnystuff"
    __bind_key__ = 'redditbot'
    __table_args__ = {'useexisting': True}
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    comment = Column(String(255))


class FoodStuff(Base2):
    __tablename__ = "foodstuff"
    __bind_key__ = 'redditbot'
    __table_args__ = {'useexisting': True}
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    comment = Column(String(255))


Base2.metadata.create_all(engine2)
