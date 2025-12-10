from database import Base
from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True)
    email = Column(String(255), unique=True)
    password = Column(String(255), nullable=False)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    orders = relationship("Order", back_populates="user")  # one-to-many relationship


    def __repr__(self):
        return f"<user>{self.username}"


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    price = Column(Integer)
    orders = relationship("Order", back_populates="product")


    def __repr__(self):
        return f"<product>{self.name}"


class Order(Base):
    ORDER_STATUS_CHOICES = (
        ('PENDING', 'pending'),
        ('IN_TRANSIT', 'in_transit'),
        ('DELIVERED', 'delivered')
    )
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    status = Column(ChoiceType(choices=ORDER_STATUS_CHOICES))
    user_id = Column(Integer, ForeignKey('user.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    user = relationship("User", back_populates="orders")  # many-to-one relationship
    product = relationship('Product', back_populates='orders')

    def __repr__(self):
        return f"<order>{self.id}>"