from project import db
from sqlalchemy import Column, Integer, Float, String, Boolean, DateTime
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql import func

# from sqlalchemy.orm import validates


class Projects(db.Model):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255))
    tags = Column(postgresql.ARRAY(String(255)))
    hourly_rate = Column(Float)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    created_by = Column(Integer, db.ForeignKey("users.id"), nullable=False)

    def __init__(self, title, description, tags, hourly_rate, created_by):
        """Constructor function for instanciation"""
        self.title = title
        self.description = description
        self.tags = tags
        self.hourly_rate = hourly_rate
        self.created_by = created_by

    def __repr__(self) -> str:
        return str(f"<Projects {self.id}:{self.title}>")
