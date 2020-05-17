from flask import (Blueprint, flash, g, redirect,
                   render_template, request, session, url_for)


about_bp = Blueprint('about', __name__, url_prefix='/about')

@about_bp.route("/")
def about_page():
    return render_template('about.html',
                           title="About",
                           header_title="About",
                           header_subtitle="me")