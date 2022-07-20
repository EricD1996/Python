from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_user
DATABASE = "july_instruments_db"

class Instrument:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.time_played = data['time_played']
        self.type = data['type']
        self.avg_price = data['avg_price']
        self.review = data['review']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['update_at']

    @classmethod
    def create(cls, data:dict) -> int:
        query = "INSERT INTO instruments (name, time_played, type, avg_price, review, user_id) VALUES (%(name)s, %(time_played)s, %(type)s, %(avg_price)s, %(review)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def get_one(cls, data:dict) -> list:
        query = "SELECT * FROM instruments WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if results:
            return cls(results[0])
        return False

    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM instruments JOIN users ON users.id = instruments.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_instruments = []
            for dict in results:
                instrument = cls(dict)
                user_data = {
                    'id': dict['users.id'],
                    'created_at': dict['created_at'],
                    'updated_at': dict['updated_at'],
                    'first_name': dict['first_name'],
                    'last_name': dict['last_name'],
                    'email': dict['email'],
                    'pw': dict['pw']
                }
                user = model_user.User(user_data)
                instrument.player = user
                all_instruments.append(instrument)
            return all_instruments
        return []

    @classmethod
    def update_one(cls, data:dict) -> None:
        query = "UPDATE instruments SET name = %(name)s, time_played = %(time_played)s, type = %(type)s, avg_price = %(avg_price)s, review = %(review)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete_one(cls, data:dict) -> None:
        query = "DELETE FROM instruments WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validator(data:dict) -> bool:
        is_valid = True

        if len(data['name']) < 1:
            flash('field is required', 'err_instruments_name')
            is_valid = False
        if len(data['time_played']) < 1:
            flash('field is required', 'err_instruments_time_played')
            is_valid = False
        if len(data['type']) < 1:
            flash('field is required', 'err_instruments_type')
            is_valid = False
        if len(data['avg_price']) < 1:
            flash('field is required', 'err_instruments_avg_price')
            is_valid = False
        if len(data['review']) < 1:
            flash('field is required', 'err_instruments_review')
            is_valid = False


        return is_valid