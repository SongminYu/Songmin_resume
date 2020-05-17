from flask import Flask

def create_app():

    app = Flask(__name__, template_folder='templates')

    from . import routes
    routes.init_app(app)
    app.add_url_rule("/", endpoint="index")

    return app