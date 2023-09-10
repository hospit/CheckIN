from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from checkin import run

scheduler = BlockingScheduler()
# scheduler.add_job(run, "interval", seconds=30)
scheduler.add_job(run, "cron", hour=17, minute=5)
scheduler.start()
