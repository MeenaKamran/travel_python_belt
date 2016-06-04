""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import time
import datetime

# def custom_strftime(format, t):
    # return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))

class Travel(Model):
    def __init__(self):
        super(Travel, self).__init__()
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
    def add_new_trip(self, data):
        query = "INSERT INTO trvlPlans (destination, plan, trvlStartDate, trvlEndDate, user_id, created_at) VALUES (:destination, :plan, :start_date, :end_date, :user_id, NOW())"
        
        data = {
                'destination': data['destination'],
                'plan' : data['plan'],
                'start_date': data['start_date'],
                'end_date': data['end_date'],
                'user_id': data['user_id']
        }
        return self.db.query_db(query, data)

    def get_other_trips(self, user_id):
    
        query = "SELECT users.name, trvlPlans.* FROM users JOIN trvlPlans ON users.id=trvlPlans.user_id WHERE trvlPlans.id NOT IN (SELECT trvlPlans.id FROM users JOIN trips ON users.id=trips.user_id JOIN trvlPlans ON trips.trvlPlan_id=trvlPlans.id WHERE users.id=:user_id)"
        data = {'user_id': user_id}
        other_trips = self.db.query_db(query, data)
        return other_trips

    def get_schd_trips(self, user_id):
        
        query = "SELECT trvlPlans.* FROM users JOIN trips ON users.id=trips.user_id JOIN trvlPlans ON trips.trvlPlan_id=trvlPlans.id WHERE users.id=:user_id"
        data = {'user_id': user_id}
        schd_trips = self.db.query_db(query, data)
        return schd_trips

    def add_to_trips(self, data):

        print "in add_to_trips"
        query = "INSERT into trips (user_id, trvlPlan_id) VALUES (:user_id, :trvlPlan_id)"
        data = {'user_id': data['user_id'], 'trvlPlan_id': data['trvlPlan_id']}
        return self.db.query_db(query, data)

    def get_destination_info(self, trip_id):
        
        query = "SELECT trvlPlans.*, users.name FROM users JOIN trvlPlans ON users.id=trvlPlans.user_id WHERE trvlPlans.id=:trip_id"
        data = {'trip_id': trip_id}
        return self.db.query_db(query, data)

    def get_other_users(self, trip_id):

        query = "SELECT users.name FROM users JOIN trips ON users.id=trips.user_id JOIN trvlPlans ON trips.trvlPlan_id=trvlPlans.id WHERE trvlPlans.id=:trip_id"
        data = {'trip_id': trip_id}
        return self.db.query_db(query, data)