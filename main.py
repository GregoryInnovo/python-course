# Python
from typing import Optional, List
from enum import Enum
from datetime import date

# Pydantic
from pydantic import BaseModel
from pydantic import Field, EmailStr
from pydantic.color import Color
from pydantic.types import PaymentCardBrand, PaymentCardNumber, constr

# FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path # specified the parameter have a body

# this var contain all the app
app = FastAPI()

# Models

class HairColor(Enum):
    white: Color= "#FFFFFF"
    brown: Color= "#964B00"
    black: Color= "#282c34"
    blonde: Color= "#f5e265"
    red: Color= "#c11b1b"


class Location(BaseModel):
    city: str = Field(
        ..., 
        min_length=1,
        max_length=50,
    )
    state: str = Field(
        ..., 
        min_length=1,
        max_length=50,
    )
    country: str = Field(
        ..., 
        min_length=1,
        max_length=50,
    )


class Person(BaseModel):
    first_name: str = Field(
        ..., 
        min_length=1,
        max_length=50,
    )
    last_name: str = Field(
        ..., 
        min_length=1,
        max_length=50,
    )
    age: int = Field(
        ..., 
        gt=0,
        le=115
    )
    email: List[EmailStr]
    # if the user dont send nothing the value is NULL
    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[bool] = Field(default=None)


class Card(BaseModel):
    name: constr(strip_whitespace=True, min_length=1)
    number: PaymentCardNumber = Field(
        ..., 
        min_length=1,
        max_length=16,
    )
    exp: date = Field(
        ..., 
        title="Expired date",
        description="This is the expired date for the card",
    )


    @property
    def brand(self) -> PaymentCardBrand:
        return self.number.brand

    @property
    def expired(self) -> bool:
        return self.exp < date.today() 




# Fast operations
@app.get("/") # path operation decorator
def home(): # path operation function
    return {"Hello": "World"}

# Request and response body
@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person

# Validations: Query params
@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
        None, 
        min_length=1, 
        max_length=50,
        title="Person name",
        description="This is the person name. It's between 1 and 50 characters",
    ),
    age: str = Query(
        ...,
        title="Person age",
        description="This is the person age. It's required",
    ),
):
    return {name: age}

# Validations: Path params
@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ..., 
        gt=0,
        title="Person id",
        description="This is the person id. It's required",
    )
):
    return {person_id: "It exists!"}

# Validations: Request body
@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        title= "Person ID",
        description= "This is the person id.",
        gt= 0,
    ),
    person: Person = Body(...),
    location: Location = Body(...),
    card: Card = Body(...),
): 
    results = person.dict()
    results.update(location.dict()) # append the dic
    results.update(card.dict())
    return results