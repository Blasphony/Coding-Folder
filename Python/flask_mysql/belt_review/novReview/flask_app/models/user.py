from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app

from flask import flash
import re # A package for regular expressions 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') # regex101.com for a testing place for regular expressions

from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)

class User:
    db_name = "your_db_name_here" # Change this string to your Workbench database name to make all these queries work

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # Associated data goes here...

    @staticmethod
    def validate_register(user): # If update form doesn't look at EVERY field used here, make a separate staticmethod
        is_valid = True
        users_with_email = User.get_by_email({"email": user['email']}) # Find any User with the email from the registration form
        print(users_with_email) # Either [{}] or False
        # Validations go here...
        return is_valid

    @classmethod
    def create_one(cls, data):
        query = "INSERT INTO users (name, email, password) VALUES (%(name)s, %(email)s, %(password)s);"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results) #ID
        return results

    @classmethod
    def get_by_email(cls, data): # For logging in + register validation
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results) #[{}]
        return cls(results[0])