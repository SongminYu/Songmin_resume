from .home import home_bp
from .projects import projects_bp
from .articles import articles_bp

def init_app(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(projects_bp)
    app.register_blueprint(articles_bp)