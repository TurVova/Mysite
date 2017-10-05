from flask import Flask
from .config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager



app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.init_app(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from . import views, models

app.add_url_rule('/', 'index', views.index)
