from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import *
from databse import Base


schemaname = "public"

class User(Base) :
    __tablename__ = "users"
    __table_args__ = {'schema':schemaname}
    UserId = Column(Integer , primary_key=True, autoincrement=True)
    Title = Column(String)
    FirstName = Column(String)
    LastName = Column(String)
    Email = Column(String)
    Username = Column(String)
    DOB = Column(String)

class Upload(Base) :
    __tablename__ = "uploads"
    __table_args__ = {'schema':schemaname}
    UploadId = Column(Integer, primary_key=True,autoincrement=True)
    UserId = Column(Integer)
    Title = Column(String)
    Body = Column(String)
    # Timestamp = Column(Date)



