from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

from db import db

app = Flask(__name__)
api = Api(app)
# da izwadim configuration = config("DEV_CONFIGURATION_LINK") w env a ne da q hardcodwame

# конфигурацията за апп-а е във файла config
app.config.from_object("config.DevelopmentConfig")
migrate = Migrate(app, db)

if __name__ == "main":
    app.run(debug=True)
