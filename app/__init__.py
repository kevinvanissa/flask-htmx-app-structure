from flask import Flask

from config import Config
from app.extensions import db, login, migrate
from app.views import before_request_func, load_user

def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)

    # Register before_request function
    app.before_request(before_request_func)

    # Initialize Flask extensions here
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    # Register user loading function
    login.user_loader(load_user)

    # Register blueprints here
    from app.views import main_bp 
    from app.views import auth_bp 
    from app.views import error_bp 

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(error_bp)

    return app
