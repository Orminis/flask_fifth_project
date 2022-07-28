from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

from db import db
from resources.routes import routes

app = Flask(__name__)
# Начин(метод) да се конфигурира и свърже app с db след като са инициализирани и създадени в други файлове
db.init_app(app)

# da izwadim configuration = config("DEV_CONFIGURATION_LINK") w env a ne da q hardcodwame
# конфигурацията за апп-а е във файла config
# app.config.from_object("config.DevelopmentConfig")
app.config.from_envvar("config.FLASK_CONFIG")

api = Api(app)
migrate = Migrate(app, db)

[api.add_resource(*route_data) for route_data in routes]

if __name__ == "__main__":
    app.run()
