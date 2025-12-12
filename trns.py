import requests
from flask import Flask, jsonify, request

# Dummy API credentials (randomized values)
API_BASE_URL = "https://api.equitas.com"  # Replace with actual API endpoint
API_KEY = "1a2b3c4d5e6f7g8h9i0jklmnop12345"  # Randomized API key
API_SECRET = "98765zyxwvutsrqponmlkjihgfedcba"  # Randomized secret key

app = Flask(__name__)

# Helper function to simulate fetching transactions
def fetch_transactions():
    url = f"{API_BASE_URL}/transactions"  # Replace with actual endpoint
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "x-api-secret": API_SECRET
    }

    # Simulating a response from the API with dummy transaction data
    transactions = [
        {"transaction_id": "T123", "amount": 1000, "status": "Success", "date": "2025-12-01"},
        {"transaction_id": "T124", "amount": 500, "status": "Failed", "date": "2025-12-02"},
        {"transaction_id": "T125", "amount": 750, "status": "Pending", "date": "2025-12-05"}
    ]
    return transactions

@app.route('/transactions', methods=['GET'])
def get_transactions():
    transactions = fetch_transactions()
    return jsonify({"status": "success", "data": transactions})

@app.route('/make-transaction', methods=['POST'])
def make_transaction():
    data = request.json  # Get JSON data from the request
    if not data.get("amount"):
        return jsonify({"error": "Amount is required"}), 400

    # Simulating a successful transaction with a new transaction ID
    transaction_id = "T126"
    transaction_data = {
        "transaction_id": transaction_id,
        "amount": data["amount"],
        "status": "Success",
        "date": "2025-12-12"
    }

    return jsonify({"status": "success", "transaction": transaction_data})

if __name__ == '__main__':
    app.run(debug=True)
