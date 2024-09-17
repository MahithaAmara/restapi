from flask import Flask, jsonify, request

app = Flask(__name__)

# Example data (you can later replace this with a database)
books = [
    {'id': 1, 'title': '1984', 'author': 'George Orwell'},
    {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'}
]

# Home route
@app.route('/')
def home():
    return "Welcome to the Book API!"

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)


if __name__ == '__main__':
    app.run(debug=True)
