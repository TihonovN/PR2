from flask import Flask, render_template, request

app = Flask(__name__)

# Пример данных о книгах
books = [
    {"title": "1984", "author": "George Orwell", "genre": "Dystopian", "pages": 328},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction", "pages": 281},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Fiction", "pages": 180},
    {"title": "Moby Dick", "author": "Herman Melville", "genre": "Adventure", "pages": 585},
    {"title": "War and Peace", "author": "Leo Tolstoy", "genre": "Historical", "pages": 1225},
    # Добавьте больше книг по мере необходимости
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    genre = request.form.get('genre')
    min_pages = int(request.form.get('min_pages', 0))
    max_pages = int(request.form.get('max_pages', float('inf')))
    author = request.form.get('author')

    filtered_books = [
        book for book in books
        if (genre == '' or book['genre'].lower() == genre.lower()) and
           (min_pages <= book['pages'] <= max_pages) and
           (author == '' or book['author'].lower() == author.lower())
    ]

    return render_template('result.html', books=filtered_books)

if __name__ == '__main__':
    app.run(debug=True)
