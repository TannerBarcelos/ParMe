<<<<<<< HEAD
=======
import os
from flask import Flask
from extensions import db
from routes.auth import auth

def create_app():

    app = Flask(__name__)
<<<<<<< HEAD
    app.register_blueprint(auth)
        # Attach the environment DB secrets to the app config
=======
    app.register_blueprint(auth, url_prefix="/api/auth")
    
    # Attach the environment DB secrets to the app config
>>>>>>> 0afddd21f77d43dce96a9adeceeb9b93f30b324a
    app.config['MYSQL_HOST'] = os.getenv("MYSQL_HOST")
    app.config['MYSQL_USER'] = os.getenv("MYSQL_USER")
    app.config['MYSQL_PASSWORD'] = os.getenv("MYSQL_PASSWORD")
    app.config['MYSQL_DB'] = os.getenv("MYSQL_DB")

    # Put in variables to make the connection string below cleaner
    dbUser = app.config['MYSQL_USER']
    dbHost = app.config['MYSQL_HOST']
    dbPass = app.config['MYSQL_PASSWORD']
    dbName = app.config['MYSQL_DB']

    # SQLAlchemy connection URI
    connectionURI = f'mysql+pymysql://{dbUser}:{dbPass}@{dbHost}/{dbName}'

    # Saving the URI to the app config 
    app.config['SQLALCHEMY_DATABASE_URI'] = connectionURI

    # Connect to AWD RDS instance
    db = pymysql.connect(host=dbHost, user=dbUser, password=dbPass, database=dbName)


    return app, db


if __name__ == '__main__':
    app, db = create_app()
    app.run(debug=True)

>>>>>>> 4ad7516a11b9cbe5d49796354fd005b08a9a8755
