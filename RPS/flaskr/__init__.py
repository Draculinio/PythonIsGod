import os
from flask import Flask

def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    from . import db
    db.init_app(app)

    return app
