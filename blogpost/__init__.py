from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from blogpost.config import Config

login_manager = LoginManager()
bootstrap = Bootstrap()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    bootstrap.init_app(app)


    from blogpost.home.routes import home
    app.register_blueprint(home)

    return app