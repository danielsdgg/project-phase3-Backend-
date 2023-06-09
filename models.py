from sqlalchemy import create_engine, String, Column, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

# phone_company=Table(
#     'phone_company',Base.metadata,
#     Column('phone_id', Integer, ForeignKey('phone_id'))

# )

class Phone(Base):
    __tablename__ = 'phones'
    id = Column(Integer, primary_key = True)
    image = Column(String())
    name = Column(String())
    brand = Column(String())
    test_performance = Column(String())
    release_date = Column(Integer)
    price = Column(Integer)

    manufacturer_id = Column(Integer, ForeignKey('manufacturers.id'))
    manufacture = relationship('Manufacturer', back_populates='phone')

    customer_id = Column(Integer, ForeignKey('customers.id'))
    custom = relationship('Customers', back_populates='phones')

class Manufacturer(Base):
    __tablename__ = 'manufacturers'
    id = Column(Integer, primary_key = True)
    name = Column(String())
    headquaters = Column(String())
    history = Column(String())

    phone = relationship('Phone', back_populates='manufacture')

class Customers(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key = True)
    fname = Column(String())
    lname = Column(String())
    email = Column(String())
    message = Column(String())

    phones = relationship('Phone', back_populates = 'custom')

class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key = True)
    order_date = Column(Integer)
    status = Column(String())

class Sales(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key = True)
    customer_id = Column(Integer)
    quantity = Column (Integer())
    price = Column(Integer())

    # Phone = relationships('phones', backref='phone_sales')


engine = create_engine('sqlite:///dan.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()