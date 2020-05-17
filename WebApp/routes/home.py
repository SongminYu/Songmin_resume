import oyaml as yaml
from flask import (Blueprint, flash, g, redirect,
                   render_template, request, session, url_for)

home_bp = Blueprint('home', __name__)

@home_bp.route("/")
def index():
    website_data = yaml.load(open('_config.yaml'))
    return render_template('index.html',
                           data=website_data)