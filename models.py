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
    is_active = Column(Boolean, default=False)
    orders= relationship("Order")


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    price = Column(Integer)


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
    user_id = Column(Integer,ForeignKey('user.id'))
    product_id = Column(Integer,ForeignKey('product.id'))
