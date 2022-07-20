from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
DATABASE = 'pets_db'
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.password = data['password']
        self.email = data['email']
        self.created_at = ['created_at']
        self.updated_at = ['updated_at']

    @classmethod
    def getAll(cls):
        query = "SELECT * FROM users"
        result = connectToMySQL(DATABASE).query_db(query)
        users = []
        for user in result:
            users.append(cls(user))
        return users

    @classmethod
    def getOneById(cls,id):
        query = "SELECT * FROM users LEFT JOIN likes on users.id = user_id WHERE users.id = %(id)s"
        data = {'id':id}
        result = connectToMySQL(DATABASE).query_db(query,data)
        user = cls(result[0])
        user.liked_shows = []
        if result[0]['show_id']:
            for row in result:
                user.liked_shows.append(row['show_id'])
            print(user.liked_shows)
        return user

    @classmethod
    def getOneByEmail(cls, email):
        query = "SELECT * FROM users WHERE email = %(email)s"
        data = {'email':email}
        result = connectToMySQL(DATABASE).query_db(query,data)
        if not result:
            return result
        return cls(result[0])

    @staticmethod
    def isValid(data):
        isValid = True
        if not EMAIL_REGEX.match(data['email']):
            flash('Email not in valid format')
            isValid = False
        all_users = User.getAll()
        for user in all_users:
            if(user.email == data['email']):
                flash('Email already in database, hope it was you!')
                isValid = False
        if(len(data['first_name']) < 2) or not data['first_name'].isalpha():
            flash('First name must be at least two characters and only letters')
            isValid = False
        if(len(data['last_name']) < 2) or not data['last_name'].isalpha():
            flash('Last name must be at least two characters and only letters')
            isValid = False
        if not data['password'] == data['password2']:
            flash('Password do not match')
            isValid = False
        if(len(data['password'] < 8)):
            flash('Password must be at least 8 characters')
            isValid = False
        if isValid:
            flash('User Created Successfully')
        return isValid

    @staticmethod
    def newUser(data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, %(created_at)s, %(updated_at)s"
        return connectToMySQL(DATABASE).query_db(query,data)