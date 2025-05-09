from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Contact(BaseModel):
    name: str
    email: str
    phone: str

@app.post("/create-contact")
def create_contact(contact: Contact):
    # Simulate contact creation
    return {
        "message": "Contact created successfully",
        "contact": contact
    }
