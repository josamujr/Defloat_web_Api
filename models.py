from main import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = 'Trina_INVESTIMENTS'

    id = Column(Integer, primary_key= True, nullable=False)
    title = Column(String(2000), nullable=False)
    content = Column(String(2000), nullable=False)

    user_id = Column(Integer, ForeignKey("USERS.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User")

class User(Base):
    __tablename__ = 'USERS'
    id = Column(Integer, primary_key= True, nullable=False)
    email = Column(String(20), nullable= False, unique= True)
    password = Column(String(200), nullable= False)


class Votes(Base):
    __tablename__ = 'VOTES'
    user_id = Column(Integer, ForeignKey("USERS.id", ondelete='CASCADE'), primary_key=True)
    post_id = Column(Integer, ForeignKey("Trina_INVESTIMENTS.id", ondelete='CASCADE'), primary_key=True)