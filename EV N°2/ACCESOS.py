# accesos.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Accesos(Base):
    __tablename__ = 'accesos'
    
    id = Column(Integer, primary_key=True)
    id_emp = Column(Integer, ForeignKey('empleados.id'))
    id_modulo = Column(Integer, ForeignKey('modulos.id'))
    
    empleado = relationship("Empleados")
    modulo = relationship("Modulos")