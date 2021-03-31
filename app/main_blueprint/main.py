
from flask import Blueprint, render_template, flash, request

from flask import current_app as app

from . import async_running

import asyncio

main_blueprint = Blueprint('main_blueprint', __name__) 

@main_blueprint.route('/', methods=['GET','POST'])
def homepage():

    post_data = request.get_json()

    print('STATE = ', post_data['state'])

    state = post_data['state']

    if state == 'on':
        print('turning sprinklers on')
        # create the task and start it? and await it's finishing..
        # check for already running?
        any_running = asyncio.current_task()
        if any_running is not None:
            return 1
        
        asyncio.run(task_loop(async_running.run_sprinklers())
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
        running_task = asyncio.current_task()
        if running_task is not None:
            return 1
        else:
            return 0


def task_loop(function):
    water_grass = asyncio.create_task(function(5))

    await water_grass