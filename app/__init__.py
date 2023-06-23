from flask import Flask


from config import Config

from .auth.routes import auth
from .ig.routes import ig
from .models import db, User
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment
from .api.routes import api
