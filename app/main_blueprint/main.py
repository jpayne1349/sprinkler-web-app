
from flask import Blueprint, render_template, flash, request

from flask import current_app as app

from . import async_running

import asyncio

main_blueprint = Blueprint('main_blueprint', __name__) 

task_loop = asyncio.new_event_loop()

@main_blueprint.route('/', methods=['GET','POST'])
def homepage():

    post_data = request.get_json()

    print('STATE = ', post_data['state'])

    state = post_data['state']

    if state == 'on':
        print('turning sprinklers on')
        # create the task and start it? and await it's finishing..
        # check for already running?
        task_loop.run_until_complete(async_running.run_sprinklers(5))
        #task_loop.create_task(async_running.run_sprinklers(5))
        # start up the asynchronous function
        # return 1 to on 
        return 1

    elif state == 'off':
        print('turning sprinklers off')
        a_task = asyncio.current_task()
        if a_task is not None:
            a_task.cancel()

        return 0
    elif state == 'update':
        # check if a loop is running?
        try:
            running = asyncio.get_running_loop()
            return 1
        except:
            running = False
            return 0

