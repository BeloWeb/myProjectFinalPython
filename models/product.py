from sqlalchemy import Column, Integer, String, Float
from .base import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    quantity = Column(Integer, default=0)
    price = Column(Float)

    def __repr__(self):
        return (f"<Product(id={self.id}, name='{self.name}', quantity={self.quantity}, "
                f"price={self.price})>")