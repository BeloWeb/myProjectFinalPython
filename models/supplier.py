from sqlalchemy import Column, Integer, String
from .base import Base

class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_info = Column(String)

    def __repr__(self):
        return f"<Supplier(id={self.id}, name='{self.name}', contact='{self.contact_info}')>"