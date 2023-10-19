from flask import Blueprint, render_template, Response
from flask_login import login_required

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')



        