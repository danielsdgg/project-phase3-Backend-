# importing libraries
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import Phone, session
from typing import List, Optional

app = FastAPI()

# create a pydantic class called Phone
class PhoneSchema(BaseModel):
    id:int
    name:str
    brand:str
    test_performance:str
    release_date:int
    price:int

# create a pydantic class called manufacturer
class ManufacturerSchema(BaseModel):
    id:int
    name:str
    headquaters:str
    history:str

class CustomerSchema(BaseModel):
    id:int
    fname:str
    lname:str
    email:str

class OrderSchema(BaseModel):
    id:int
    order_date:int
    status=str

class SaleSchema(BaseModel):
    id:int
    quantity:int
    price:int
    customer_id = int

class Config:
    orm_mode = True

# Creating a pydantic class called UpdatePhone
class UpdatePhoneSchema(BaseModel):
    id:Optional[int] = None
    name:Optional[str] = None
    release_date:Optional[int] = None
    price:Optional[int] = None

    # Creating a component that returns a list of all phones
@app.get('/phones')
def root() -> List[PhoneSchema]:
    phone = session.query(Phone).all()
    return phone

# Creating a component that returns a single phone that we choose
@app.get('/phones/{id}')
def get_single_phone(id: int):
    phone = session.query(Phone).filter_by(id=id).first()
    if phone is None:
        raise HTTPException(status_code=404, detail="Phone does not exist in our database")
    return phone

# Creating a component that adds to our list  a new phone and its details
@app.post('/add_phone')
def add_data (cell: PhoneSchema) :
    pns = Phone(**dict(cell))
    session.add(pns)
    session.commit()
    return cell

# Creating a component that edits specific details of a phone we choose
@app.patch('/phones/update/{id}')
def update_phone(id:int,payload:UpdatePhoneSchema):
    pns = session.query(Phone).filter_by(id=id).first()
    for key,value in dict(payload).items():
        setattr(pns,key,value)
        session.commit()
        return {"detail":f"Phone is fully edited"}
    
# Creating a component that edits all details of a phone
@app.put('/full_updates/{id}')
def full_update(id:int,payload:UpdatePhoneSchema):
    pns = session.query(Phone).filter_by(id=id).first()
    for key,value in dict(payload).items():
            setattr(pns,key,value)
            session.commit()
            return {"detail":f"Phone is completely edited"}
    
 # Creating a component that deletes a phone
@app.delete('/phones/{id}')
def delete_phone (id:int) -> None:
    pns = session.query(Phone).filter_by(id=id).first()
    session.delete(pns)
    session.commit()
    return{"detail":f"phone with id{id} has been deleted successfully"}