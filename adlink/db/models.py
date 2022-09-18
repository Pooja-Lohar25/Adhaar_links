
from .schemas import *
from sqlalchemy import UniqueConstraint
import uuid
from sqlalchemy import UniqueConstraint
# class User_data(SQLModel,table=True): #storing user info in db
#     Adhaar : str= Field(primary_key=True)
#     username:str
#     hashed_password: str 
#     disabled: bool

class agency_data(SQLModel,table=True): #storing organisation info in db
    __table_args__ = (UniqueConstraint('agency_id'),)
    agency_id:str = Field(primary_key=True)
    ag_uniq_id:str 
    agency_Name:str
    hashedpass:str

class user_req_agency(SQLModel,table=True): #user requesting any agency 
    reqid:str = Field(primary_key=True)
    agencyid:str = Field(foreign_key = "agency_data.agency_id")
    adhaar:str 
    custid:str
    fetched_data:str 
    status:str = Field(default = "0")

class demo_user(SQLModel,table = True):
    adhaar : str = Field(primary_key = True)
    name:str
    address:str
    phone:str
    
class demo_linked_agencies(SQLModel,table = True):
    id:Optional[int]=Field(primary_key=True)
    adhaar :str = Field(foreign_key = demo_user.adhaar)
    agency_id:str 
    ag_name : str
    custid : str
