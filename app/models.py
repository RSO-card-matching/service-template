# pylint: disable=no-name-in-module

from typing import Optional

from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Column, Integer, String


Base = declarative_base()


class Sample(BaseModel):
    id: int
    name: str
    remark: Optional[str] = None

class SampleModel(Base):
    __tablename__ = "sample"
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, index = True)
    remark = Column(String)
