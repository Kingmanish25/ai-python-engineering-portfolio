import schedule
import time

def job():
    print("Scheduled task running")

schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
