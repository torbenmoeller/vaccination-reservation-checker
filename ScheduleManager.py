import sched
import time

import ReservationCheck

five_seconds = 5
priority = 1
ten_minutes = 60 * 10
scheduler = sched.scheduler(time.time, time.sleep)


def start_run():
    ReservationCheck.check_for_appointments()
    scheduler.enter(ten_minutes, priority, start_run)


def start():
    scheduler.enter(five_seconds, priority, start_run, scheduler)
    scheduler.run()


if __name__ == "__main__":
    start()
