# proyecto.py
from sqlalchemy import Column, Integer, String, Date, Boolean

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Proyecto(Base):
    __tablename__ = 'proyecto'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    descripcion = Column(String(500))
    fecha_inicio = Column(Date)
    fecha_fin = Column(Date)
    validar_fechas = Column(Boolean)