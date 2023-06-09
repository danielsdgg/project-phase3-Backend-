# importing libraries
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import Phone, Customers,Manufacturer,Sales, session
from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

origins=[
    'http://localhost:3000'
]

app.add_middleware  (
   CORSMiddleware,
   allow_origins = origins,
   allow_credentials = True,
   allow_methods = ["*"],
   allow_headers = ["*"],
)

# create a pydantic class called Phone
class PhoneSchema(BaseModel):
    id:int
    image:str
    name:str
    brand:str
    test_performance:str
    release_date:int
    price:int
    manufacturer_id:int
    customer_id:int
    
    class Config:
        orm_mode = True

# create a pydantic class called manufacturer
class ManufacturerSchema(BaseModel):
    id:int
    name:str
    headquaters:str
    history:str

    class Config:
        orm_mode = True

class CustomerSchema(BaseModel):
    id:int
    fname:str
    lname:str
    email:str
    mesaage:str

    class Config:
        orm_mode = True

class OrderSchema(BaseModel):
    id:int
    order_date:int
    status=str

    class Config:
        orm_mode = True

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

# Creating a pydantic class called Updatemanufacturer
class UpdateManufacturerSchema(BaseModel):
    id:Optional[int] = None
    name:Optional[str] = None
    headquaters:Optional[str] = None
    history:Optional[str] = None

# Creating a pydantic class called Updatecustomer
class UpdateCustomerSchema(BaseModel):
    id:Optional[int] = None
    fname:Optional[str] = None
    lname:Optional[str] = None
    email:Optional[str] = None

# Creating a pydantic class called Updatesale
class UpdateSaleSchema(BaseModel):
    id:Optional[int] = None
    quantity:Optional[str] = None
    price:Optional[int] = None
    customer_id:Optional[int] = None


    # Creating a component that returns a list of all phones
@app.get('/phones')
def root() -> List[PhoneSchema]:
    phone = session.query(Phone).all()
    return phone

# Creating a component that returns a single phone that we choose
@app.get('/phones/{id}', response_model=PhoneSchema)
def get_single_phone(id: int):
    phone = session.query(Phone).filter_by(id=id).first()
    if phone is None:
        raise HTTPException(status_code=404, detail="Phone does not exist in our database")
    return phone

# Creating a component that adds to our list  a new phone and its details
@app.post('/add_phone')
def add_phone (cell: PhoneSchema) :
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
@app.delete('/deletephones/{id}')
def delete_phone (id:int) -> None:
    pns = session.query(Phone).filter_by(id=id).first()
    session.delete(pns)
    session.commit()
    return{"detail":f"phone with id{id} has been deleted successfully"}


# # Manufacturer
# # Creating a component that returns a list of all manufacturers
@app.get('/manufacturers')
def root() -> List[ManufacturerSchema]:
    maker = session.query(Manufacturer).all()
    return maker

# # Creating a component that returns a single manufacturer
@app.get('/manufacturers/{id}')
def get_a_manufacturer(id: int):
    man = session.query(Manufacturer).filter_by(id=id).first()
    if man is None:
        raise HTTPException(status_code=404, detail="Manufacturer does not exist in our database")
    return man

# # Creating a component that adds to our list  a new manufacturer
@app.post('/add_manufacturer')
def add_maker (supply: ManufacturerSchema) :
    mkr = Manufacturer(**dict(supply))
    session.add(mkr)
    session.commit()
    return supply

# # Creating a component that edits details of manufacturer
@app.put('/update_manufacturer/{id}')
def update_manufacturer(id:int,payload:UpdateManufacturerSchema):
    pns = session.query(Manufacturer).filter_by(id=id).first()
    for key,value in dict(payload).items():
            setattr(pns,key,value)
            session.commit()
            return {"detail":f"Manufacturer is completely edited"}



# # Customers
# # Creating a component that returns a list of all customers
@app.get('/customers')
def root() -> List[CustomerSchema]:
    cust = session.query(Customers).all()
    return cust

# # Creating a component that returns a single customer
@app.get('/customers/{id}')
def get_one_customer(id: int):
    custom = session.query(Customers).filter_by(id=id).first()
    if custom is None:
        raise HTTPException(status_code=404, detail="Customer does not exist in our database")
    return custom

# # Creating a component that adds to our list  a new customer
@app.post('/add_customer')
def add_customer (person: CustomerSchema) :
    cms = Customers(**dict(person))
    session.add(cms)
    session.commit()
    return person

# # Creating a component that edits details of customer
@app.put('/update_customer/{id}')
def update_customer(id:int,payload:UpdateCustomerSchema):
    pns = session.query(Customers).filter_by(id=id).first()
    for key,value in dict(payload).items():
            setattr(pns,key,value)
            session.commit()
            return {"detail":f"Customer has been edited"}


# # Sales
# # creating a component that return a list of sales
@app.get('sales')
def root() -> List[SaleSchema]:
    goods = session.query(Sales).all()
    return goods

# # creating a component that returns a single sale
@app.get('/sales/{id}')
def get_one_sale(id:int):
    stuff = session.query(SaleSchema).filter_by(id=id).first()
    if stuff is None:
        raise HTTPException(status_code=404, detail="Sale does not exist")
    return stuff

# # Creating a component that adds to our list  a new sale
@app.post('/add_sale')
def add_sale (money: SaleSchema) :
    buy = Sales(**dict(money))
    session.add(buy)
    session.commit()
    return money

# # Creating a component that edits details of sale
@app.put('/update_sale/{id}')
def update_sale(id:int,payload:UpdateSaleSchema):
    pns = session.query(Sales).filter_by(id=id).first()
    for key,value in dict(payload).items():
            setattr(pns,key,value)
            session.commit()
            return {"detail":f"Sale has been updated"}