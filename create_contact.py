from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# In-memory contact storage (you can replace this with a database later)
contacts = []

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/create_contact', methods=['POST'])
def create_contact():
    # Get JSON data from request
    contact_data = request.get_json()

    # Extract contact details (you can modify this as per your needs)
    name = contact_data.get('name')
    phone = contact_data.get('phone')
    email = contact_data.get('email')

    if not name or not phone or not email:
        return jsonify({"error": "Missing contact details"}), 400

    # Store the contact (in-memory for now)
    contacts.append({
        'name': name,
        'phone': phone,
        'email': email
    })

    return jsonify({"message": "Contact created successfully", "contact": contact_data}), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
