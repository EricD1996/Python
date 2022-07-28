from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_user
DATABASE = "tv_shows"

class Show:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.network = data['network']
        self.date = data['date']
        self.description = data['description']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data:dict) -> int:
        query = "INSERT INTO shows (name, network, date, description, user_id) VALUES (%(name)s, %(network)s, %(date)s, %(description)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_one(cls, data:dict) -> list:
        query = "SELECT * FROM shows WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if results:
            return cls(results[0])
        return False

    @classmethod
    def get_one_by_id(cls, data):
        query = "SELECT * FROM shows JOIN users on users.id = shows.user_id WHERE shows.id = %(id)s"
        result = connectToMySQL(DATABASE).query_db(query,data)
        for dict in result:
            show = cls(result[0])
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
            show.poster = poster
        return show

    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM shows JOIN users ON users.id = shows.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_shows = []
            for dict in results:
                show = cls(dict)
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
                show.maker = user
                all_shows.append(show)
            return all_shows
        return []

    @classmethod
    def update_one(cls, data:dict) -> None:
        query = "UPDATE shows SET name = %(name)s, network = %(network)s, date = %(date)s, description = %(description)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete_one(cls, data:dict) -> None:
        query = "DELETE FROM shows WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validator(data:dict) -> bool:
        is_valid = True

        if len(data['name']) < 1:
            flash('Name is required', 'err_shows_name')
            is_valid = False
        if len(data['network']) < 1:
            flash('Network is required', 'err_shows_network')
            is_valid = False
        if len(data['date']) < 1:
            flash('Date is required', 'err_shows_date')
            is_valid = False
        if len(data['description']) < 3:
            flash('Description is Required, must be at least 3 characters', 'err_shows_description')
            is_valid = False        

        return is_valid