from flask_app.config.mysqlconnection import connectToMySQL
from .book import Book

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.favorite_books = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.books = []
        
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors"
        
        results = connectToMySQL('books_schema').query_db(query)
        authors = []
        
        for i in results:
            authors.append(cls(i))
        return authors
    
    @classmethod
    def save(cls, data):
        query="INSERT INTO authors (name) VALUES (%(name)s);"
        result = connectToMySQL('books_schema').query_db(query,data)
        return result
    
    @classmethod
    def get_one_with_books(cls,data):
        query = "SELECT * FROM authors LEFT JOIN authors_has_books ON authors.id = authors_has_books.authors_id LEFT JOIN books ON books.id = authors_has_books.books_id WHERE authors.id = %(id)s;"
        results = connectToMySQL('books_schema').query_db(query,data)
        print(results)
        author = cls(results[0])
        for row in results:
            data = {
                'id' : row['books.id'],
                'title' : row['books.title'],
                'num_of_pages' : row['books.num_of_pages'],
                'created_at': row['books.created_at'],
                'updated_at': row['books.updated_at']
            }
            author.authors_has_books.append(Book(data))
        return author