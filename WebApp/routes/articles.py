from flask import (Blueprint, flash, g, redirect,
                   render_template, request, session, url_for)


articles_bp = Blueprint('articles', __name__, url_prefix='/articles')

@articles_bp.route("/")
def articles_page():
    return render_template('articles.html',
                           title="Articles",
                           header_title="Articles",
                           header_subtitle="")