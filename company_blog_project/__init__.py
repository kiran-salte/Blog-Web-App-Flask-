import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = 'mysecret'
##Database##

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

##login configrations

login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'

from company_blog_project.core.views import core
from company_blog_project.users.views import users
from company_blog_project.blog_posts.views import blog_posts
from company_blog_project.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(blog_posts)
app.register_blueprint(error_pages)
