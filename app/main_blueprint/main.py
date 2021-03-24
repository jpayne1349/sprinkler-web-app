
from flask import Blueprint, render_template, flash, request

from flask import current_app as app

main_blueprint = Blueprint('main_blueprint', __name__) 


@main_blueprint.route('/', methods=['GET','POST'])
def homepage():

    post_data = request.get_json(force=True)

    print(post_data)

    return render_template('homepage.html')
