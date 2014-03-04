from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String, Boolean

class Agency(Base):
  __tablename__ = 'agencies'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  has_direction = Column(Boolean)
  mode = Column(String)
