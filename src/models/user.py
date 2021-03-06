from sqlalchemy import Column, DateTime, Integer, String, BigInteger, Date, DateTime, Float, Index,  Table, Text, Time, text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    address = Column(String(50), nullable=False)
    password = Column(String(500), nullable=False)

    def __str__(self):
        return "User(id='%s')" % self.id
