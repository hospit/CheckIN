from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from checkin import run
import time

# scheduler = BlockingScheduler()
# # scheduler.add_job(run, "interval", seconds=30)
# scheduler.add_job(run, "cron", hour=18, minute=43)
# scheduler.start()
while True:
    seconds = 60
    time.sleep(seconds)
    try:
        run()
    except:
        print("出现错误")

