from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_user
DATABASE = "recipe_db"

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.data_cooked = data['data_cooked']
        self.under_30 = data['under_30']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data:dict) -> int:
        query = "INSERT INTO recipes (name, description, instructions, data_cooked, under_30, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(data_cooked)s, %(under_30)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_one(cls, data:dict) -> list:
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if results:
            return cls(results[0])
        return False

    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_recipes = []
            for dict in results:
                recipe = cls(dict)
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
                recipe.maker = user
                all_recipes.append(recipe)
            return all_recipes
        return []

    @classmethod
    def update_one(cls, data:dict) -> None:
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, data_cooked = %(data_cooked)s, under_30 = %(under_30)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete_one(cls, data:dict) -> None:
        query = "DELETE FROM recipes WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validator(data:dict) -> bool:
        is_valid = True

        if len(data['name']) < 1:
            flash('Name is required', 'err_recipes_name')
            is_valid = False
        if len(data['description']) < 1:
            flash('Description is required', 'err_recipes_description')
            is_valid = False
        if len(data['instructions']) < 1:
            flash('Instruction is required', 'err_recipes_instructions')
            is_valid = False
        if len(data['data_cooked']) < 1:
            flash('Date is Required', 'err_recipes_data_cooked')
            is_valid = False
        if "under_30" not in data:
            flash('field is required', 'err_recipes_under_30')
            is_valid = False
        

        return is_valid