from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/create_contact', methods=['POST'])
def create_contact():
    data = request.get_json()  # Get JSON data from the request
    # Assuming you want to store the contact data (could be in a database)
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')

    # Here, you can process the data (e.g., store in a database)
    contact = {"name": name, "email": email, "phone": phone}

    return jsonify({"message": "Contact created", "contact": contact}), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
