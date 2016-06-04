""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class User(Model):
    def __init__(self):
        super(User, self).__init__()
    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """
    def create_user(self, info):
        # We write our validations in model functions.
        # They will look similar to those we wrote in Flask
        # EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-za-z]*$')
        errors = []
        # datetime.datetime.now()
        # Some basic validation
      
        if not info['name']:
            errors.append('First Name cannot be blank')

        elif len(info['name']) < 3:
            errors.append('First Name must be at least 3 characters long')
        
        if len(info['username']) < 3:
            errors.append('Username must be at least 3 characters long')

        if not info['password']:
            errors.append('Password cannot be blank')
        elif len(info['password']) < 8:
            errors.append('Password must be at least 8 characters long')
        elif info['password'] != info['pw_confirmation']:
            errors.append('Password and confirmation must match!')
        
        # If we hit errors, return them, else return True.
        if errors:

            return {"status": False, "errors": errors}
        else:
            pw_hash = self.bcrypt.generate_password_hash(info['password'])
            # Code to insert user goes here...
            query_insert="INSERT INTO users (name, username, password, created_at) VALUES (:name, :username, :password, NOW())"
            data={'name':info['name'], 'username':info['username'],'password':pw_hash}
            self.db.query_db(query_insert, data)
            # Then retrieve the last inserted user.
            get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
            users = self.db.query_db(get_user_query)

            status = { "status": True, "user": users[0] }
            return status

    def login(self, info):

        errors = []
       
        query_login = "SELECT * FROM users WHERE username = :username LIMIT 1"
        data = { 'username': info['username'] }
        
        user = self.db.query_db(query_login, data)
        
        # print user
        if user == []:

            errors.append('Invalid login!')
            return{"status": False, "errors": errors}
        else:
            if self.bcrypt.check_password_hash(user[0]['password'], info['password']):

                return {"status": True, "user": user[0] }
            else:

                errors.append('Invalid password!')
                return{"status": False, "errors": errors}
