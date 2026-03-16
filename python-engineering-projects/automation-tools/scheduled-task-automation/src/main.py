import schedule
import time
import argparse
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def job():
    logging.info("Scheduled task running")


def run_scheduler(interval):

    schedule.every(interval).seconds.do(job)

    logging.info(f"Task scheduled every {interval} seconds")

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)

    except KeyboardInterrupt:
        logging.info("Scheduler stopped by user")


def main():

    parser = argparse.ArgumentParser(description="Scheduled Task Automation Tool")

    parser.add_argument(
        "--interval",
        type=int,
        default=10,
        help="Interval in seconds between scheduled tasks"
    )

    args = parser.parse_args()

    run_scheduler(args.interval)


if __name__ == "__main__":
    main()
