#!/usr/bin/python3
"""
State module that controls the state model
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
from models import storageType


class State(BaseModel, Base):
    """
    State class that inherit from BaseModel
    """
    if storageType == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref="state",
                              cascade="all, delete")
    else:
        name = ""

        @property
        def cities(self):
            """Get a list of all related City objects.
            """
            city_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
