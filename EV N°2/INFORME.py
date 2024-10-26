# informe.py
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Informe(Base):
    __tablename__ = 'informe'
    
    id = Column(Integer, primary_key=True)
    nombre_informe = Column(String(100))
    fecha_creacion = Column(Date)
    id_empleado = Column(Integer, ForeignKey('empleados.id'))
    utilizacion = Column(String(200))
    
    empleado = relationship("Empleados")