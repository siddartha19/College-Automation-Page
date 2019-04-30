#!/usr/bin/env python3
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    rollno = Column(String(10), nullable=False)
    gmail = Column(String(250), nullable=False)
    phoneno = Column(String(10), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'rollno': self.rollno,
            'gmail': self.gmail,
            'phoneno': self.phoneno,
        }


class Attendance(Base):
    __tablename__ = 'attendance'

    id = Column(Integer, primary_key=True)
    rollno = Column(String(10), nullable=False)
    day = Column(String(50), nullable=False)
    subject = Column(String(50), nullable=False)
    period = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'rollno': self.rollno,
            'day': self.day,
            'subject': self.subject,
            'period': self.period,
        }



engine = create_engine('sqlite:///students.db')
Base.metadata.create_all(engine)
