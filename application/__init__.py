##makes it importable module ___init__.py
import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://emtltuyg:xLTVPR_b-y4pVf8pb0lhHcfUOHTGhIuY@trumpet.db.elephantsql.com/emtltuyg"
##instance of the db
db = SQLAlchemy(app)

## need to make sure it is after what has been initialized 
from application import routes

# pipenv install psycopg2
