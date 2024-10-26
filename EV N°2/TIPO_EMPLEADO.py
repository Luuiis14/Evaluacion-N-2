# tipo_empleado.py
from sqlalchemy import Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
Base = declarative_base()
class TipoEmpleado(Base):
    __tablename__ = 'tipo_empleado'
    
    id = Column(Integer, primary_key=True)
    tipo = Column(String(50))
    detalle = Column(String(200))