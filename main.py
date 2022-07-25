from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

from db import db

app = Flask(__name__)
api = Api(app)
migrate = Migrate(app, db)

if __name__ == "main":
    app.run(debug=True)
