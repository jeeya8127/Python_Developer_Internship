from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "username": "alice", "email": "alice@example.com"},
    {"id": 2, "username": "bob", "email": "bob@example.com"}
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user is None:
        return jsonify({"message": "User not found"}), 404
    return jsonify(user)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'username' not in data or 'email' not in data:
        return jsonify({"message": "Missing required fields"}), 400
    
    new_id = max([u['id'] for u in users]) + 1 if users else 1
    new_user = {
        "id": new_id,
        "username": data['username'],
        "email": data['email']
    }
    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user is None:
        return jsonify({"message": "User not found"}), 404
    
    data = request.get_json()
    if not data:
        return jsonify({"message": "No update data provided"}), 400
        
    user.update({
        "username": data.get("username", user["username"]),
        "email": data.get("email", user["email"])
    })
    return jsonify(user)

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    user_index = next((i for i, u in enumerate(users) if u['id'] == user_id), -1)
    
    if user_index == -1:
        return jsonify({"message": "User not found"}), 404
        
    users.pop(user_index)
    return jsonify({"message": "User deleted"}), 204

if __name__ == '__main__':
    app.run(debug=True)