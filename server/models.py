from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Column, String, Integer

# contains definitions of tables and associated schema constructs
metadata = MetaData()

# create the Flask SQLAlchemy extension
db = SQLAlchemy(metadata=metadata)

# define a model class by inheriting from db.Model.


class Employee(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    salary = db.Column(db.Integer)

    def __repr__(self):
        return f'<Employee {self.id}, {self.name}, {self.salary}>'

class Department(db.Model):
    __tablename__= 'department'

    id = Column(Integer(), primary_key= True, autoincrement=True)
    name= Column(String(), nullable = False)
    location= Column(String())

    def __repr__ (self):
        return f'<id:{self.id}'+ \
        f'name: {self.name}' + \
        f'adress:{self.location}>'