from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User

class Sasq:
    db_name = 'sasquatch'

    def __init__(self,db_data):
        print(db_data)
        self.id = db_data['id']
        self.location = db_data['location']
        self.description = db_data['description']
        self.num_of_sasq = db_data['num_of_sasq']
        self.date_siting = db_data['date_siting']
        self.user_id = db_data['user_id']
        user = User.get_by_id({'id': db_data['user_id']})
        self.name = user.first_name +" "+ user.last_name
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO sasq (location, description, num_of_sasq, date_siting, user_id) VALUES (%(location)s,%(description)s,%(num_of_sasq)s,%(date_siting)s,%(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM sasq;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_sasq = []
        for row in results:
            print(row['date_siting'])
            all_sasq.append( cls(row) )
        return all_sasq
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM sasq WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls( results[0] )

    @classmethod
    def update(cls, data):
        query = "UPDATE sasq SET location=%(location)s, description=%(description)s, num_of_sasq=%(num_of_sasq)s, date_siting=%(date_siting)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM sasq WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @staticmethod
    def validate_sasq(sasq):
        is_valid = True
        if len(sasq['location']) < 3:
            is_valid = False
            flash("Location must be filled in","sasq")
        if int(sasq['num_of_sasq']) < 1:
            is_valid = False
            flash("Number of Sasquatches must be at least 1","sasq")
        if len(sasq['description']) < 5:
            is_valid = False
            flash("Description must be filled in","sasq")
        if sasq['date_siting'] == "":
            is_valid = False
            flash("date_siting must be filled in","sasq")
        return is_valid
