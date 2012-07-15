# -*- coding: utf-8 -*-
from sqlalchemy.orm import mapper, relationship
from sqlalchemy import Table, Column, Integer, String, MetaData, Unicode, UnicodeText, UniqueConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from bartendro.utils import session, Base

class DrinkLog(Base):
    """
    Keeps a record of everything we've dispensed
    """

    __tablename__ = 'drink_log'
    id = Column(Integer, primary_key=True)
    drink_id = Column(Integer, ForeignKey('drink.id'), nullable=False)
    time = Column(Integer, nullable=False, default=0)
    size = Column(Integer, nullable=False, default=-1)
 
    query = session.query_property()

    def __init__(self, drink_id, time, size):
        self.drink_id = drink_id
        self.time = time
        self.size = size
        session.add(self)

    def __repr__(self):
        return "<DrinkLog(%d,'%s')>" % (self.id, self.drink_id)

