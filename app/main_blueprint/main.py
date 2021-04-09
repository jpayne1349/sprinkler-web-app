
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

    print('queue found - ', current_app.rq_inst.get_queue())

    if state == 'on':
        print('turning sprinklers on')
        sprinkler_job = runSprinklers.fake_run.queue(1)
        
        print('job id = ', sprinkler_job.get_id())
        print('job status = ', sprinkler_job.get_status())
        return '1'

    elif state == 'off':
        print('turning sprinklers off')
        job = rq.job.Job.fetch('sprinkler_job', connection=current_app.redis)
        status = job.get_status()
        print('running job status =', status)
        if status == 'started':
            rq.command.send_stop_job_command(current_app.redis, 'sprinkler_job')
            # actually need to then queue the stop function to close valves?
            closing_valves = current_app.task_queue.enqueue(runSprinklers.stop, job_id='stopping_job')

        return '0'

    elif state == 'update':
        
        worker = current_app.rq_inst.get_worker()
        print('Worker Object', worker)
        print('Worker State', worker.state)
        print(worker.pid)

        if not worker:
            print('no worker found')
            return '0'
        else:
            state = worker.state
            print('worker state = ', state)

        if state == 'busy':
            return '1'
        else:
            return '0'

       
