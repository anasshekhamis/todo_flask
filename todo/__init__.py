from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

#@TODO: Use application factory approach
app = Flask(__name__)
# This is just for the front-end to be able to send requests
CORS(app)
app.config.from_object('todo.config.Config')
db = SQLAlchemy(app)

# register blueprints
from todo.api_v1 import api as api_blueprint
app.register_blueprint(api_blueprint, url_prefix='/api/v1')
