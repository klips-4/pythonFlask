from Model.BaseModel import BaseModel

from sqlalchemy import Column, Text, DateTime, ForeignKey, Integer


class Patient(BaseModel):
    __tablename__ = 'patients'

    person_id = Column(Integer, ForeignKey('person_info.id'))
    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    comment = Column(Text)
    date_birthay = Column(DateTime, nullable=False)
    date_in = Column(DateTime, nullable=False)
    date_out = Column(DateTime)

    person_info = relationship('PersonInfo', lazy='join',
                               foreign_keys=[person_id])
    doctor = relationship('Doctor', lazy='join',
                               foreign_keys=[doctor_id])
