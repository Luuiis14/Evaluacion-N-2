# modulos.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Modulos(Base):
    __tablename__ = 'modulos'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))