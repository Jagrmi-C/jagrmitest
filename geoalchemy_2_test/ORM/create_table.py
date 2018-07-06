from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2 import Geometry
from sqlalchemy import Column, Integer, String

from geoalchemy_2_test.ORM import engine

Base = declarative_base()


class Lake(Base):
    __tablename__ = 'lake'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    geom = Column(Geometry('POLYGON'))


print(Lake.__table__)
Lake.__table__.create(engine.engine)
