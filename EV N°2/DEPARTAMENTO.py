# departamento.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Departamento(Base):
    __tablename__ = 'departamento'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    telefono = Column(String(20))
    id_empleado = Column(Integer, ForeignKey('empleados.id'))
    
    empleado = relationship("Empleados")