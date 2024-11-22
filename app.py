from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Kết nối tới database
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "password"),
        database=os.getenv("DB_NAME", "test_db"),
    )

# Endpoint kiểm tra
@app.route("/")
def home():
    return "Hello from Flask + MySQL!"

# Endpoint thêm dữ liệu
@app.route("/add", methods=["POST"])
def add_record():
    data = request.json
    name = data.get("name")

    if not name:
        return jsonify({"error": "Name is required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": f"User {name} added successfully!"})

# Endpoint lấy dữ liệu
@app.route("/users", methods=["GET"])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = [{"id": row[0], "name": row[1]} for row in cursor.fetchall()]
    cursor.close()
    conn.close()

    return jsonify(users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
