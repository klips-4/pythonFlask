from sqlalchemy import Column, Text, DateTime, ForeignKey, Integer, Boolean
from Model.BaseModel import BaseModel

class Service(BaseModel):
    __tablename__ = 'services'

    name = Column(Text, nullable=False)
    price = Column(DECIMAL, default=0)
    description = Column(Text)
    is_active = Column(Boolean, default=True)




