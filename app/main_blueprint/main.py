
from flask import Blueprint, render_template, flash, request

from flask import current_app as app

from . import runSprinklers


main_blueprint = Blueprint('main_blueprint', __name__) 


@main_blueprint.route('/', methods=['GET','POST'])
def homepage():

    post_data = request.get_json()

    print('STATE = ', post_data['state'])

    state = post_data['state']

    if state == 'on':
        print('turning sprinklers on')
        runSprinklers.run(5)
    elif state == 'off':
        print('turning sprinklers off')
        runSprinklers.stop()
    elif state == 'update':
        code = runSprinklers.getStatus()
        print('return status code = ', code)
        return code