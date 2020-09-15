from redis import Redis
from rq_scheduler import Scheduler
import rq 
from datetime import datetime, timedelta
from .blockchain_compare import compare_campaign_value
    
def set_up_workers(app):
    app.redis = Redis.from_url(app.config['REDIS_URL'])
    app.task_queue = rq.Queue('ethoboost-tasks', connection=app.redis)
    app.scheduler = Scheduler(queue=app.task_queue, connection=app.redis)
    clear_scheduled_jobs(app.scheduler)
    app.scheduler.schedule(
        scheduled_time = datetime.utcnow(),
        # func = compare_campaign_value,
        func = 'src.tasks.blockchain_compare.compare_campaign_value',
        # Can't pass in app
        # args = [app],
        interval = 15,
        repeat = None
    )


def ten_seconds():
    current_time = datetime.utcnow()
    return current_time + timedelta(seconds=10)

def clear_scheduled_jobs(scheduler): 
    for job in scheduler.get_jobs(): 
        print("Deleting scheduled job %s", job)
        job.delete()