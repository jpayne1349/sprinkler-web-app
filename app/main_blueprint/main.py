
from flask import Blueprint, render_template, flash, request

from flask import current_app as app

import rq

main_blueprint = Blueprint('main_blueprint', __name__) 

task_loop = asyncio.new_event_loop()

@main_blueprint.route('/', methods=['GET','POST'])
def homepage():

    post_data = request.get_json()

    print('STATE = ', post_data['state'])

    state = post_data['state']

    if state == 'on':
        print('turning sprinklers on')
        sprinkler_job = current_app.task_queue.enqueue('app.main_blueprint.runSprinklers.fake_run', 1, job_timeout=600, job_id='sprinkler_job')
        print('job id = ', sprinkler_job.job_id)
        return '1'

    elif state == 'off':
        print('turning sprinklers off')
        job = rq.job.fetch('sprinkler_job', connection=current_app.redis)
        status = job.get_status()
        print(status)
        if status == 'started':
            rq.command.send_stop_job_command(current_app.redis, job.job_id)
        return '0'

    elif state == 'update':
        # check if a loop is running?
        workers = rq.Worker.all(connection=current_app.redis)
        worker = workers[0]
        if worker.state == 'started':
            return '1'
        else:
            return '0'

       
