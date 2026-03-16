from device_connector import connect_to_device
from config_manager import push_configuration
from monitoring import monitor_device


DEVICES = [
    {"host": "192.168.1.10", "vendor": "cisco"},
    {"host": "192.168.1.11", "vendor": "juniper"}
]


def run_automation():

    for device in DEVICES:

        print(f"\nConnecting to device {device['host']}")

        connection = connect_to_device(device["host"])

        if connection:

            push_configuration(connection, device["vendor"])

            monitor_device(connection)

        else:

            print("Connection failed")


if __name__ == "__main__":
    run_automation()
