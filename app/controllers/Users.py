"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        try: 
            session['name']
            session['id']

        except:
            session['name']=" "
            session['id']=0
        self.load_model('User')
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
        return self.load_view('index.html')

    def create(self):
        user_info = {
             "name" : request.form['form-name'],
             "username": request.form['form-username'],
             "password":request.form['form-password'],
             "pw_confirmation" : request.form['form-conf-password']
        }
        print request.form['form-username']
        
        # call create_user method from model and write some logic based on the returned value
        # notice how we passed the user_info to our model method
        # print "before create_status is called"
        create_status = self.models['User'].create_user(user_info)
        #print create_status
  
        if create_status['status'] == True:
            # print "we are in create_status = true"
            # the user should have been created in the model
            # we can set the newly-created users id and name to session
            session['id'] = create_status['user']['id'] 
            session['name'] = create_status['user']['name']
            # we can redirect to the users profile page here
            # print "before calling success.html"
            return redirect('/travels')
        else:
            # set flashed error messages here from the error messages we returned from the Model
            for message in create_status['errors']:
                flash(message, 'regis_errors')
            # redirect to the method that renders the form
            return redirect('/')

    def login(self):
        user_info = {
            "username" : request.form['form-username'],
            "password" : request.form['form-password']
        }
        # print "before calling create_status"
        create_status = self.models['User'].login(user_info)
        # print "after calling create_status"
        if create_status['status'] == True:
            # print "we are in create_status=True"
            session['id'] = create_status['user']['id']
            session['name'] = create_status['user']['name']
            # print session['id']
            return redirect('/travels')
        else:
            # set flashed error messages here from the error messages we returned from the Model
            for message in create_status['errors']:
                flash(message, 'regis_errors')
            return redirect('/')

    def logout(self):
        session['id'] = 0
        session['name'] = ""
        return redirect('/')



