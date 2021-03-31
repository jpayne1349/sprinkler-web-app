
from flask import Blueprint, render_template, flash, request, current_app

import rq

from . import runSprinklers

main_blueprint = Blueprint('main_blueprint', __name__) 

@main_blueprint.route('/', methods=['GET','POST'])
def homepage():

    post_data = request.get_json()

    print('STATE = ', post_data['state'])

    state = post_data['state']

    print('task_queue ?', current_app.task_queue)

    if state == 'on':
        print('turning sprinklers on')
        sprinkler_job = current_app.task_queue.enqueue(runSprinklers.fake_run, 1)
        print('job id = ', sprinkler_job.get_id())
        print('job status = ', sprinkler_job.get_status())
        return '1'

    elif state == 'off':
        print('turning sprinklers off')
        job = rq.job.Job.fetch('sprinkler_job', connection=current_app.redis)
        status = job.get_status()
        print(status)
        if status == 'started':
            rq.command.send_stop_job_command(current_app.redis, 'sprinkler_job')
        return '0'

    elif state == 'update':
        worker = current_app.worker
        state = worker.state
        queues = worker.queues
        print(worker)
        print('worker state', state)
        print('worker queues', queues)
        if state == 'started':
            return '1'
        else:
            return '0'

       
