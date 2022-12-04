#!/usr/bin/python3
# Defines a State model.
# Inherits from SQLAlchemy Base and links to the MySQL table states.
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City

class State(Base):
    """Represents a state for a MYSQL database.

    Attributes:
        __tablename__(str): The name of the MySQL table to store States.
        id (sqlalchemy.Integer): The state's id.
        name (sqlalchemy.String): The state's name.
        cities (sqlalchemy.orm.relationship): The State-City relationship.
    """
    __tablename__ = "States"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
