# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Contact(BaseModel):
#     name: str
#     email: str
#     phone: str

# @app.post("/create-contact")
# def create_contact(contact: Contact):
#     # Simulate contact creation
#     return {
#         "message": "Contact created successfully",
#         "contact": contact
#     }


from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
