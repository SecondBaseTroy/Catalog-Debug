import os
import sys
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


def get_current_time():
    return datetime.datetime.now()


class Category(Base):
    # create key(s) for table
    # automatically updates on creation and update
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    date = Column(DateTime, default=get_current_time,
                  onupdate=get_current_time)

    def __init__(self, name):
        self.name = name

    @property
    def serialize(self):
        """Return serializeable format of the Category Object"""
        return {
            'name': self.name,
            'id': self.id,
        }


class CategoryItem(Base):
    __tablename__ = 'category_item'

    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=False)
    owner = Column(String(20), nullable=False)
    description = Column(String(250), nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    date = Column(DateTime, default=get_current_time,
                  onupdate=get_current_time)

    def __init__(self, title, owner, description, category_id):
        self.title = title
        self.owner = owner
        self.description = description
        self.category_id = category_id

    @property
    def serialize(self):
        """Return serializeable format of the Category Item Object"""
        return {
            'id': self.id,
            'owner': self.owner,
            'title': self.title,
            'description': self.description,
        }

engine = create_engine('sqlite:///catalogshoes.db')

Base.metadata.create_all(engine)
