import psutil
import time
import argparse
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def monitor():

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    logging.info(f"CPU Usage: {cpu}%")
    logging.info(f"Memory Usage: {memory}%")


def start_monitor(interval):

    logging.info(f"System monitoring started (interval: {interval} seconds)")

    try:
        while True:
            monitor()
            time.sleep(interval)

    except KeyboardInterrupt:
        logging.info("System monitoring stopped by user")


def main():

    parser = argparse.ArgumentParser(description="System Resource Monitor")

    parser.add_argument(
        "--interval",
        type=int,
        default=5,
        help="Monitoring interval in seconds"
    )

    args = parser.parse_args()

    start_monitor(args.interval)


if __name__ == "__main__":
    main()
