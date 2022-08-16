from dataclasses import dataclass
from project import db

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import validates

@dataclass
class Project(db.Model):
    """Project Model for Handling Projects Informations."""
    id:int
    pname:str
    sampling_type:str
    description:str
    instructions:str
    is_active:bool
    created_by:int
    created_at:int

    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    pname = Column(String(255), nullable=False)
    sampling_type = Column(String(20), nullable=False)
    description = Column(String(255))
    instructions = Column(String(255))
    is_active = Column(Boolean(), default=True)
    created_by = Column(Integer, db.ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __init__(self, pname, sampling_type, description, instructions, created_by):
        """Project Model Constructor"""
        self.pname = pname
        self.sampling_type = sampling_type
        self.description = description
        self.instructions = instructions
        self.created_by = created_by

    def __repr__(self):
        """Project Model Object Representation"""
        return str(f"<Project {self.pname} {self.sampling_type}>")
