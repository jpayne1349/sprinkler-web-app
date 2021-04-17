
from flask import Blueprint, render_template, flash, request, current_app

from . import runSprinklers

main_blueprint = Blueprint('main_blueprint', __name__) 

@main_blueprint.route('/', methods=['GET','POST'])
def homepage():

    if request.method == 'GET':
        return render_template('homepage.html')

    post_data = request.get_json()

    print('STATE = ', post_data['state'])

    state = post_data['state']
