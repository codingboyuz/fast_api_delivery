from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType


class User(Base):
    __tablename__ = 'users'   # ❗ o‘zgardi

    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True, index=True)
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255), nullable=False)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

    orders = relationship("Order", back_populates="user")

    def __repr__(self):
        return f"<User {self.username}>"


class Product(Base):
    __tablename__ = 'products'  # ❗ o‘zgardi

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    price = Column(Integer)

    orders = relationship("Order", back_populates="product")

    def __repr__(self):
        return f"<Product {self.name}>"


class Order(Base):
    __tablename__ = 'orders'   # ❗ o‘zgardi

    ORDER_STATUS_CHOICES = (
        ('PENDING', 'pending'),
        ('IN_TRANSIT', 'in_transit'),
        ('DELIVERED', 'delivered')
    )

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    status = Column(ChoiceType(choices=ORDER_STATUS_CHOICES))

    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))

    user = relationship("User", back_populates="orders")
    product = relationship("Product", back_populates="orders")

    def __repr__(self):
        return f"<Order {self.id}>"
