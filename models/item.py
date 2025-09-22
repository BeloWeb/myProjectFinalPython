from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    quantity = Column(Integer, default=0)
    price = Column(Float, nullable=False)

    category_id = Column(Integer, ForeignKey('categories.id'))
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))

    category = relationship('Category', backref='items')
    supplier = relationship('Supplier', backref='items')

    def __repr__(self):
        return (f"<Item(id={self.id}, name='{self.name}', quantity={self.quantity}, "
                f"price={self.price}, category={self.category.name if self.category else None}, "
                f"supplier={self.supplier.name if self.supplier else None})>")