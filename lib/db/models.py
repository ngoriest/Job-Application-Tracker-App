from sqlalchemy import Column, Integer, DateTime, String, Text, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime, date

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    applications = relationship("Application", back_populates="user")

class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(255))
    is_active = Column(Boolean, default=True)

class Application(Base):
    __tablename__ = 'applications'

    id = Column(Integer, primary_key=True, autoincrement=True)
    company_name = Column(String(100), nullable=False)
    job_title = Column(String(100), nullable=False)
    status = Column(String(50), nullable=False)
    application_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    deadline = Column(DateTime)
    notes = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="applications")
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    category = relationship("Category")
    

