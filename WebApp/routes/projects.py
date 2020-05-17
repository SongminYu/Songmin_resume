from flask import (Blueprint, flash, g, redirect,
                   render_template, request, session, url_for)


projects_bp = Blueprint('projects', __name__, url_prefix='/projects')

@projects_bp.route("/")
def projects_page():
    return render_template('projects.html',
                           title="Projects",
                           header_title="Projects",
                           header_subtitle="things I do")