# proyecto_empleado.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class ProyectoEmpleado(Base):
    __tablename__ = 'proyecto_empleado'
    
    id = Column(Integer, primary_key=True)
    id_proyecto = Column(Integer, ForeignKey('proyecto.id'))
    id_empleado = Column(Integer, ForeignKey('empleados.id'))
    
    proyecto = relationship("Proyecto")
    empleado = relationship("Empleados")