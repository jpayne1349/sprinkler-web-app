
from flask import Blueprint, render_template, flash, request

from flask import current_app as app

from . import runSprinklers

from multiprocessing import Process

main_blueprint = Blueprint('main_blueprint', __name__) 

@main_blueprint.route('/', methods=['GET','POST'])
def homepage():

    running = Process(target=runSprinklers.run, args=(5,))

    post_data = request.get_json()

    print('STATE = ', post_data['state'])

    state = post_data['state']

    if state == 'on':
        print('turning sprinklers on')
        running.start()
        return '1'
    elif state == 'off':
        print('turning sprinklers off')
        running.terminate()
        runSprinklers.stop()
        return '0'
    elif state == 'update':
        if running.is_alive():
            print(' status = 1')
            return '1'
        else:
            print(' status = 0')
            return '0'