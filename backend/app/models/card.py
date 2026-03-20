"""Credit card and card reward database models."""

from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.db.base import Base
from enum import Enum as PyEnum


class Card(Base):
    """Credit card model."""

    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    card_name = Column(String(255), nullable=False, index=True)
    issuer = Column(String(255), nullable=False)  # e.g., 'HDFC', 'ICICI'
    annual_fee = Column(Float, default=0.0)  # Annual fee in rupees
    reward_points_per_rupee = Column(Float, default=1.0)  # Base reward rate

    # Relationships
    rewards = relationship("CardReward", back_populates="card", cascade="all, delete-orphan")


class CardReward(Base):
    """Card reward rates by category."""

    __tablename__ = "card_rewards"

    id = Column(Integer, primary_key=True, index=True)
    card_id = Column(Integer, ForeignKey("cards.id"), nullable=False, index=True)
    category = Column(String(100), nullable=False)  # e.g., 'groceries', 'travel', 'dining'
    reward_percentage = Column(Float, nullable=False)  # e.g., 2.5 for 2.5% cashback

    # Relationships
    card = relationship("Card", back_populates="rewards")
