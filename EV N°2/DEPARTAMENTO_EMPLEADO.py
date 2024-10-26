# departamento_empleado.py
from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class DepartamentoEmpleado(Base):
    __tablename__ = 'departamento_empleado'
    
    id = Column(Integer, primary_key=True)
    id_depto = Column(Integer, ForeignKey('departamento.id'))
    id_empleado = Column(Integer, ForeignKey('empleados.id'))
    validar_asignacion = Column(Boolean)
    
    departamento = relationship("Departamento")
    empleado = relationship("Empleados")