from sqlalchemy import Column, Integer, String, Text, ForeignKey, TIMESTAMP, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    progress = relationship("Progress", back_populates="user")

class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    difficulty_level = Column(String(50))
    created_at = Column(TIMESTAMP, server_default=func.now())

    progress = relationship("Progress", back_populates="activity")

class Progress(Base):
    __tablename__ = "progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    activity_id = Column(Integer, ForeignKey("activities.id", ondelete="CASCADE"))
    score = Column(Integer)
    completed_at = Column(TIMESTAMP, server_default=func.now())

    user = relationship("User", back_populates="progress")
    activity = relationship("Activity", back_populates="progress")
