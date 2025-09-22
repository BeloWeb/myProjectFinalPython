from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base

class InventoryMovement(Base):
    __tablename__ = 'inventory_movements'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity_change = Column(Integer, nullable=False)
    movement_type = Column(String)  # 'entry' ou 'exit'
    date = Column(DateTime, default=datetime.utcnow)

    product = relationship("Product")

    def __repr__(self):
        return (f"<InventoryMovement(id={self.id}, product_id={self.product_id}, "
                f"quantity_change={self.quantity_change}, type={self.movement_type}, date={self.date})>")