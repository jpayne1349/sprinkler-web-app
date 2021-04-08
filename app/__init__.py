
from flask import Flask, current_app
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from redis import Redis
from flask_rq2 import RQ

db = SQLAlchemy()
migrate = Migrate()
rq = RQ()

# login_manager = LoginManager() # USE FOR LOGIN PAGE IF NEEDED

def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)

    app.config.from_object('config.DevelopmentConfig') # grabbing the development config class out of config.py
    # our config file will be located elsewhere

    db.init_app(app)
    migrate.init_app(app, db)
    rq.init_app(app)

    app.rq_inst = rq

    #login_manager.init_app(app) # USE FOR LOGIN PAGE IF NEEDED

    #login_manager.login_view = 'authorization_bp.login_page' # USE FOR LOGIN PAGE IF NEEDED

    with app.app_context():

        from .main_blueprint import main # giving the app access to this folder and this file

        app.register_blueprint(main.main_blueprint)  # registering the blueprint inside that file

        
        #from . import models  # USED WHEN DB IS NEEDED
        
        
    
        return app


