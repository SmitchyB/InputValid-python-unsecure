from flask import Flask, request, jsonify
from flask_cors import CORS 

app = Flask(__name__)
# Enable CORS for all origins. This is essential for your React frontend
# to communicate with this backend, as they will likely be on different ports.
CORS(app)

# Unsecure Sign-Up Endpoint
@app.route('/signup', methods=['POST'])
def signup():
    # THIS IS THE UNSECURE PART:
    # We are directly accessing the JSON data from the request body
    # without any validation, sanitization, or checks for malicious content,
    # length, or format.
    # In a real unsecure scenario, this data might be directly
    # inserted into a database, leading to SQL injection, XSS, etc.
    data = request.get_json()

    if not data:
        # If no JSON data is sent, return an error (basic check, not validation)
        return jsonify({"message": "No data provided"}), 400

    username = data.get('username')
    email = data.get('email')
    phoneNumber = data.get('phoneNumber')
    password = data.get('password')
    confirmPassword = data.get('confirmPassword')

    # Log the RAW, UNVALIDATED data received (for demonstration purposes)
    print('--- RECEIVED UNSECURE SIGN-UP DATA ---')
    print(f'Username: "{username}"')
    print(f'Email: "{email}"')
    print(f'Phone Number: "{phoneNumber}"')
    print(f'Password: "{password}"') # In a real app, never log raw passwords!
    print(f'Confirm Password: "{confirmPassword}"')
    print('-------------------------------------')

    # Simulate a successful response as if the data was "processed"
    # even though it was not validated.
    return jsonify({"message": "Sign-up data received (unvalidated)!"}), 200

# Run the Flask app
# Use a different port (e.g., 5002) to distinguish from Node.js backends
if __name__ == '__main__':
    print("Python Flask Unsecure Backend listening at http://127.0.0.1:5002")
    print("Ready to receive unvalidated sign-up data.")
    app.run(debug=True, port=5002) # debug=True is for development, don't use in production