# from flask import Flask, request, jsonify
# import os

# app = Flask(__name__)

# # In-memory contact storage (you can replace this with a database later)
# contacts = []

# @app.route('/')
# def home():
#     return "Hello, World!"

# @app.route('/create_contact', methods=['POST'])
# def create_contact():
#     # Get JSON data from request
#     contact_data = request.get_json()

#     # Extract contact details (you can modify this as per your needs)
#     name = contact_data.get('name')
#     phone = contact_data.get('phone')
#     email = contact_data.get('email')

#     if not name or not phone or not email:
#         return jsonify({"error": "Missing contact details"}), 400

#     # Store the contact (in-memory for now)
#     contacts.append({
#         'name': name,
#         'phone': phone,
#         'email': email
#     })

#     return jsonify({"message": "Contact created successfully", "contact": contact_data}), 201

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))


from flask import Flask, request, jsonify
import os
import sqlite3

app = Flask(__name__)

# Create DB and table if not exists
def init_db():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            phone TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route("/create_contact", methods=["POST"])
def create_contact():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")

    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
    conn.commit()
    conn.close()

    return jsonify({
        "message": "Contact created successfully",
        "contact": {
            "name": name,
            "email": email,
            "phone": phone
        }
    }), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
