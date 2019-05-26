from flask import Flask  # import the Flask class from the flask module
from flask_bootstrap import Bootstrap
from config import config_options  # import config_options from the config file
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_simplemde import SimpleMDE
from flask_mail import Mail
bootstrap = Bootstrap()  # creation of Bootstrap instance
db = SQLAlchemy()  # creation of a database instance
photos = UploadSet('photos', IMAGES)
mail = Mail()
simple = SimpleMDE()
login_manager = LoginManager()  # creation of an instance of the class
# attribute that provides security levels
login_manager.session_protection = 'strong'
# prefix denotes the location of the blueprint
login_manager.login_view = 'auth.login'