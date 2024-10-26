# registro_tiempo.py
from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class RegistroTiempo(Base):
    __tablename__ = 'registro_tiempo'
    
    id = Column(Integer, primary_key=True)
    fecha = Column(Date)
    tareas = Column(String(500))
    id_asignacion = Column(Integer)
    observacion = Column(String(500))
    validar_horas = Column(Boolean)