import os
import sqlite3
from flask import Flask
from flask_restful import Api
from city import City
app=Flask(__name__)
app.secret_key='nihal'
DATABASE=os.path.join(os.getcwd(), 'dbs/data.db')
api = Api(app)

api.add_resource(City,'/city')
app.run()
