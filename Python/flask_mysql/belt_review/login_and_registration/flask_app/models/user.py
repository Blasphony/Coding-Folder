from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import sessions

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @staticmethod
    def validate_data(data):
        is_valid = True # we assume this is true
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        results = connectToMySQL("login_reg").query_db(query,data)
        if len(results) >= 1:
            flash("Email already taken.")
            is_valid=False
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid Email!!!")
            is_valid=False
            
        if len(data['first_name']) < 2:
            flash("First Name must be at least 2 characters.")
            is_valid = False
        if len(data['last_name']) < 2:
            flash("Last Name must be at least 2 characters.")
            is_valid = False
        if len(data['password']) < 8:
            flash("Bun must be at least 8 characters.")
            is_valid = False
        if data['password'] != data['confirm']:
            flash("Password must match")
            is_valid = False
        return is_valid

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s),%(password)s);"
        # comes back as the new row id
        result = connectToMySQL('login_reg').query_db(query,data)
        return result
    @classmethod
    def get_by_id(cls,data):
        query = 'SELECT * FROM users WHERE id = %(id)s'
        results = connectToMySQL('login_reg').query_db(query,data)
        return cls(results[0])
    
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.login).query_db(query)
        users = []
        for row in results:
            users.append( cls(row))
        return users