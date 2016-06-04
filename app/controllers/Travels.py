"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
import datetime

class Travels(Controller):
    def __init__(self, action):
        super(Travels, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('Travel')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
    
    def index(self):
        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """
        schd_trips = self.models['Travel'].get_schd_trips(session['id'])
        other_trips = self.models['Travel'].get_other_trips(session['id'])
        return self.load_view('travels.html', schd_trips=schd_trips, other_trips=other_trips)

    def add(self):
        return self.load_view('add_trip.html')

    def add_trip(self):
        
        data_info = {
                'destination' : request.form['destination'],
                'plan':request.form['description'],
                'start_date':request.form['trvl_start_date'],
                'end_date':request.form['trvl_end_date'],
                'user_id':session['id']
                }

        self.models['Travel'].add_new_trip(data_info)
        return redirect('/travels')

    def join_trip(self, trip_id):

        data_info = {
                    'user_id': session['id'],
                    'trvlPlan_id': trip_id
                    }
        self.models['Travel'].add_to_trips(data_info)
        print "in join_trip"
        return redirect('/travels')

    def show_destination(self, trip_id):

        dest_info = self.models['Travel'].get_destination_info(trip_id)
        users = self.models['Travel'].get_other_users(trip_id)

        return self.load_view('trip_info.html', dest_info=dest_info[0], users=users)
        

