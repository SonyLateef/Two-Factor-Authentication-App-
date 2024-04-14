from datetime import datetime

import pyotp
from flask_login import UserMixin

from src import bcrypt, db
from config import Config


class User(UserMixin, db.Model):

    __tablename__ = "users"

    #stores primary key for the users table
    id = db.Column(db.Integer, primary_key=True)
    #username of the user
    username = db.Column(db.String, unique=True, nullable=False)
    #hashed password of the user
    password = db.Column(db.String, nullable=False)
    #time when the account was created 
    created_at = db.Column(db.DateTime, nullable=False)
    #Stores the 2fa status of the user, default when accoutn is created is FALSE
    is_two_factor_authentication_enabled = db.Column(
        db.Boolean, nullable=False, default=False)
    #Unique token for each user that is created, used for enabling 2fa
    secret_token = db.Column(db.String, unique=True)

    #consturctor that intializes user
    def __init__(self, username, password):
        #initilizes users name
        self.username = username
        #hashing username password
        self.password = bcrypt.generate_password_hash(password)
        #time user was created 
        self.created_at = datetime.now()
        #unique token
        self.secret_token = pyotp.random_base32()

    #this method generates a URI which allows internet protocols to 
    #interact between and among the user's username and the application name.
    #It is used by authenticator apps like Google authenticator
    def get_authentication_setup_uri(self):
        return pyotp.totp.TOTP(self.secret_token).provisioning_uri(
            name=self.username, issuer_name=Config.APP_NAME)
    #verifies if user enters correct OTP, returns True if it matches.
    def is_otp_valid(self, user_otp):
        totp = pyotp.parse_uri(self.get_authentication_setup_uri())
        return totp.verify(user_otp)
    #to string of the user object
    def __repr__(self):
        return f"<user {self.username}>"
