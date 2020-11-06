from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Comment(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True, index=True)
    image_id = Column(Integer)
    name = Column(String)
    description = Column(String)
    