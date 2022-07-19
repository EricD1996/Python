# Setting up a flask app
- Create project/ assignment folder
- Navigate into folder
    '''
    cd project_name
    '''
- Install our virtual environment with flask, pymysql, flask-bcrypt
    '''
    pipenv install flask pymysql flask-bcrypt

    OR

    python -m pipenv install flask pymysql flask-bcrypt
    '''

'WARNING' look for pipfile and pipfile.lock!!!
- launch shell

    '''
    pipenv shell

    OR

    python -m pipenv shell
    '''

- launch VS Code in the file location
    '''
    code . 
    '''

- Build the file structure
    - project (folder)
        - flask_app (folder)
            - config (folder)
                - mysqlconnection.py
            - controllers (folder)
                - controller_user.py
            - models (folder)
                - model_user.py
            - templates (folder)
                - index.html
                - table_name_action.py
                - user_new.html
                - user_edit.html
            - static (folder)
                - css (folder)
                    - style.css
                - js (folder)
                    - script.js
            - \_\___init__ (file)
        - server.py
        - pipfile
        - pipfile.lock


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
    '''

- controller_user.py
    '''
        
    '''