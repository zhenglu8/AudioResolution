import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyBx097kuW0poFUqlrunNR73z34n3bRQMt0",
    'authDomain': "audioresolution-3f39a.firebaseapp.com",
    'databaseURL':"https://audioresolution-3f39a-default-rtdb.firebaseio.com",
    'projectId': "audioresolution-3f39a",
    'storageBucket': "audioresolution-3f39a.appspot.com",
    'messagingSenderId': "371585477300",
    'appId': "1:371585477300:web:8be8ae7369bfe290e205e1",
    'measurementId': "G-4X0GK0GBJD"
  }

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Login function
def login(email, password):
    login = auth.sign_in_with_email_and_password(email, password)
    return


# Signup Function
def signup(email, password):
    user = auth.create_user_with_email_and_password(email, password)
    return


