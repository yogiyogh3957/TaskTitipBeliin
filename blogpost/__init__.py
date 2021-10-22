from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from blogpost.config import Config

login_manager = LoginManager()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    Bootstrap(app)


    from blogpost.home.routes import home
    app.register_blueprint(home)

    return app