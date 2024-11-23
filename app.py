from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Hàm kết nối đến database
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="db",        # Tên service database trong docker-compose.yml
            user="root",      # Username của MySQL
            password="root",  # Mật khẩu của MySQL
            database="library_db"  # Database cần kết nối
        )
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# API: Lấy danh sách sách
@app.route("/books", methods=["GET"])
def get_books():
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500

    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    cursor.close()
    connection.close()

    return jsonify(books)

# API: Thêm sách mới
@app.route("/books", methods=["POST"])
def add_book():
    data = request.get_json()
    title = data.get("title")
    author = data.get("author")

    if not title or not author:
        return jsonify({"error": "Title and author are required"}), 400

    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500

    cursor = connection.cursor()
    cursor.execute("INSERT INTO books (title, author) VALUES (%s, %s)", (title, author))
    connection.commit()
    cursor.close()
    connection.close()

    return jsonify({"message": "Book added successfully"}), 201

# API: Xóa sách theo ID
@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500

    cursor = connection.cursor()
    cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
    connection.commit()
    cursor.close()
    connection.close()

    return jsonify({"message": "Book deleted successfully"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
