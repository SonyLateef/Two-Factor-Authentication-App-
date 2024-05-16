# Python 2FA using Google Authenticator, Flask, PyOTP

## Introduction: 

Our project aims to understanding the fundamentals of two-factor authentication by looking into vulnerabilities across systems, utilizing Python and the libraries for advanced 2FA features, and going further by developing a user-friendly website to host our 2FA application. One of the main tools we use is Google Authenticator in conjunction with other Python libaries such as PyOTP for one time passcode generations, QR code libraries, and many more. Our project is entirely built using Flask. 


## Setup and Use: 

To setup our 2FA application for the first time, you would have to follow the instructions below: 

1. Initialize database by running `flask db init` in the terminal (have to run this for the first time setup)
2. Migrate database changes by running `flask db migrate` in the terminal
3. Apply migrations by running `flask db upgrade` in the terminal

** For first-time run of the application, you have to run all the commands above. When changes are made to the database later, you will 
only need to run the last two commands. 

4. After running all of the commands above, you can run `python run manage.py` in the terminal to start using the application. The
application will be served on the following domain: http://127.0.0.1:5000/
