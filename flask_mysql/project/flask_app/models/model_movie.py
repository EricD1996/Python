from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_user
DATABASE = "movies"

class Movie:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.date = data['date']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def create(cls, data:dict) -> int:
        query = "INSERT INTO movies (title, description, date, user_id) VALUES (%(title)s, %(description)s, %(date)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query,data)
        
    @classmethod
    def get_one(cls, data:dict) -> list:
        query = "SELECT * FROM movies WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if results:
            return cls(results[0])
        return False

    @classmethod
    def get_one_by_id(cls, data):
        query = "SELECT * FROM movies JOIN users on users.id = movies.user_id WHERE movies.id = %(id)s"
        result = connectToMySQL(DATABASE).query_db(query,data)
        for dict in result:
            movie = cls(result[0])
            user_data = {
                'id': dict['users.id'],
                'first_name': dict['first_name'],
                'last_name': dict['last_name'],
                'pw': dict['pw'],
                'email': dict['email'],
                'created_at': dict['created_at'],
                'updated_at': dict['updated_at']                
            }
            poster = model_user.User(user_data)
            movie.poster = poster
        return movie

    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM movies JOIN users ON users.id = movies.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_movies = []
            for dict in results:
                movie = cls(dict)
                user_data = {
                    'id': dict['users.id'],
                    'first_name': dict['first_name'],
                    'last_name': dict['last_name'],
                    'pw': dict['pw'],
                    'email': dict['email'],
                    'created_at': dict['created_at'],
                    'updated_at': dict['updated_at']    
                }
                user = model_user.User(user_data)
                movie.maker = user
                all_movies.append(movie)
            return all_movies
        return []

    @classmethod
    def update_one(cls, data:dict) -> None:
        query = "UPDATE movies SET title = %(title)s, description = %(description)s, date = %(date)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete_one(cls, data:dict) -> None:
        query = "DELETE FROM movies WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validator(data:dict) -> bool:
        is_valid = True

        if len(data['title']) < 1:
            flash('Title is required', 'err_movies_title')
            is_valid = False
        if len(data['description']) < 1:
            flash('Description is Required, must be at least 3 characters', 'err_movies_description')
            is_valid = False
        if len(data['date']) < 1:
            flash('Date is required', 'err_movies_date')
            is_valid = False    

        return is_valid