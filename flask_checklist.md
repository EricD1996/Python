

# Setting up a flask app
[] Create project/assignment folder
[]Navigate into folder

    cd project_name


[] install our virtual environment with flask, pymysql, flask-bcrypt


    pipenv install flask pymysql flask-bcrypt


[]'WARNING' look for pipfile and pipfile.lock!!!

[]launch shell

    pipenv shell

[]laundh VS Code in the file location

    code .

- Build the fil structure
    - project (folder)
        - flask_app(folder)
            - config (folder)
                - [mysqlconnection.py]
            - controllers (folder)
                - [controller_user.py]
            - models (folder)
                - [model_user.py]
            - static (folder)
                - css (folder)
                    - style.css
                - js (folder)
                    - script.js
            - templates (folder)
                - index.html
                - table_name_action.py
                - user_new.html
                - user_edit.html
            - \_\_init__ (file)
        - pipfile
        - pipfile.lock
        - server.py


## mysqlconnection.py
    '''
        # a cursor is the object we use to interact with the database
        import pymysql.cursors
        # this class will give us an instance of a connection to our database
        class MySQLConnection:
            def __init__(self, db):
                # change the user and password as needed
                connection = pymysql.connect(host = 'localhost',
                                            user = 'root', 
                                            password = 'root', 
                                            db = db,
                                            charset = 'utf8mb4',
                                            cursorclass = pymysql.cursors.DictCursor,
                                            autocommit = True)
                # establish the connection to the database
                self.connection = connection
            # the method to query the database
            def query_db(self, query, data=None):
                with self.connection.cursor() as cursor:
                    try:
                        query = cursor.mogrify(query, data)
                        print("Running Query:", query)
            
                        cursor.execute(query, data)
                        if query.lower().find("insert") >= 0:
                            # INSERT queries will return the ID NUMBER of the row inserted
                            self.connection.commit()
                            return cursor.lastrowid
                        elif query.lower().find("select") >= 0:
                            # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                            result = cursor.fetchall()
                            return result
                        else:
                            # UPDATE and DELETE queries will return nothing
                            self.connection.commit()
                    except Exception as e:
                        # if the query fails the method will return FALSE
                        print("Something went wrong", e)
                        return False
                    finally:
                        # close the connection
                        self.connection.close() 
        # connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
        def connectToMySQL(db):
            return MySQLConnection(db)

## controller_user.py

    '''

    from flask_app import app, bcrypt
    from flask import render_template, redirect, session, request
    from flask_app.models import model_table_name

    #Display Route
    @app.route('/table_name/new')
    def table_name_new():
        return render_template('table_name_new.html')

    # Action Route
    @app.route('/table_name/create', methods=['POST'])
    def table_name_create():
        return redirect('/')

    #Display Route
    @app.route('/table_name/<int:id>')
    def table_name_show(id):
        return render_template('table_name_show.html')

    #Display Route
    @app.route('/table_name/<int:id>/edit')
    def table_name_edit(id):
        return render_template('table_name_edit.html')

    #Action Route
    @app.route('/table_name/<int:id>/update', methods=['POST'])
    def table_name_update(id):
        return redirect('/')

    #Action Route
    @app.route('/table_name/<int:id>/delete')
    def table_name_delete(id):
        return redirect('/')

    '''

## model_user.py

    '''py

    from flask_app.config.mysqlconnection import connectToMySQL
    from flask import flash
    
    DATABASE = "schema_name_here"

    class table_name:
        def __init__(self, data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data:dict) -> int:
        query = "INSERT INTO table_name (column_name) VALUES (%(column_name)s);"
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def get_one(cls, data:dict) -> list:
        query = "SELECT * FROM table_name WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if results:
            return cls(results[0])
        return False

    @classmethod
    def get_all(cls) -> list:
        query = "Select * FROM table_name;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_table_name = []
            for table_name_single in results:
                all_table_name.append(cls(table_name_single))
            return all_table_name
        return False

    @classmethod
    def update_one(cls, data:dict) -> None:
        query = "UPDATE table_name SET column_name = %(column_name)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete_one(cls, data:dict) -> None:
        query = "DELETE FROM table_name WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validator(data:dict) -> bool:
        is_valid = True

        # some code logic here

        return is_valid
    '''

## \_\_init__.py
    from flask import Flask
    app = Flask(__name__)
    app.secret_key = "4f7123f5-cc71-4d24-827e-b9030b650e72"
    DATABASE = 'scehma name'
    from flask_bcrypt import Bcrypt
    bcrypt = Bcrypt(app)


## server.py
    from flask_app import app
    from flask_app.controllers import controller_user

    if __name__=="__main__":
        app.run(debug=True)




