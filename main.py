from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

from db import db
from resources.routes import routes

app = Flask(__name__)
# da izwadim configuration = config("DEV_CONFIGURATION_LINK") w env a ne da q hardcodwame

# конфигурацията за апп-а е във файла config
app.config.from_object("config.DevelopmentConfig")

api = Api(app)
migrate = Migrate(app, db)

[api.add_resource(*route_data) for route_data in routes ]

# Начин(метод) да се конфигурира и свърже app с db след като
# са инициализирани и създадени апп и дб в други файлове
db.init_app(app)




if __name__ == "main":
    app.run(debug=True)
