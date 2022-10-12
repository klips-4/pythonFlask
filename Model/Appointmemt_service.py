from sqlalchemy import Column, Text, DateTime, ForeignKey, Integer, Boolean
from Model.BaseModel import BaseModel


class AppointmentService(BaseModel):
    __tablename__ = 'appointment_services'

    patient_id = Column(Integer, ForeignKey('patients.id'))
    service_id = Column(Integer, ForeignKey('services.id'))
    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    count = Column(Integer, nullable=False)
    date_complete = Column(DateTime)
    date_appointmemt = Column(DateTime, nullable=False)

    doctor = relationship('Doctor', lazy='join',
                          foreign_keys=[doctor_id])

    patient = relationship('Patient', lazy='join',
                           foreign_keys=[patient_id])

    service = relationship('Service', lazy='join',
                           foreign_keys=[service_id])
