"""Product database model (e-commerce products)."""

from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base


class Product(Base):
    """E-commerce product model."""

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(500), nullable=False, index=True)
    price = Column(Float, nullable=False)  # Price in rupees
    category = Column(String(100), nullable=False, index=True)
    platform = Column(String(100), nullable=False)  # e.g., 'Amazon', 'Flipkart'
    discount_percentage = Column(Float, default=0.0)  # Current discount
    asin_or_sku = Column(String(255), unique=True, index=True)  # Product identifier
