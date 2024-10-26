# empleados.py
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Empleados(Base):
    __tablename__ = 'empleados'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    direccion = Column(String(200))
    telefono = Column(String(20))
    correo = Column(String(100))
    fecha_inicio = Column(Date)
    salario = Column(Float)
    id_tipo = Column(Integer, ForeignKey('tipo_empleado.id'))
    rut = Column(String(20))
    contrasena = Column(String(100))
    validar_datos = Column(Boolean)
    inscriptar = Column(Boolean)
    desinscriptar = Column(Boolean)
    
    tipo_empleado = relationship("TipoEmpleado")