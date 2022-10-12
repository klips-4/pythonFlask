from sqlalchemy import Column, Text, DateTime, ForeignKey, Integer, Boolean
from Model.BaseModel import BaseModel


class Accural(BaseModel):
    __tablename__ = 'accurals'

    patient_id = Column(Integer, ForeignKey('patients.id'))
    sum = Column(DECIMAL, default=0)
    date = Column(DateTime, nullable=False)

    patient = relationship('Patient', lazy='join',
                           foreign_keys=[patients_id])
