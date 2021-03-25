
from flask import Blueprint, render_template, flash, request

from flask import current_app as app

from . import runSprinklers

from multiprocessing import Process

main_blueprint = Blueprint('main_blueprint', __name__) 

running = Process(target=runSprinklers.run, args=(5,))

@main_blueprint.route('/', methods=['GET','POST'])
def homepage():

    post_data = request.get_json()

    print('STATE = ', post_data['state'])

    state = post_data['state']

    if state == 'on':
        print('turning sprinklers on')
        running.start()
    elif state == 'off':
        print('turning sprinklers off')
        running.terminate()
        runSprinklers.stop()
    elif state == 'update':
        if running.isActive():
            return '1'
        else:
            return '0'