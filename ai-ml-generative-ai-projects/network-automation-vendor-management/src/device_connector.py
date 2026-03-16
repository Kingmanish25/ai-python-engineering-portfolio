from netmiko import ConnectHandler


USERNAME = "admin"
PASSWORD = "admin123"


def connect_to_device(host):

    device = {
        "device_type": "cisco_ios",
        "host": host,
        "username": USERNAME,
        "password": PASSWORD
    }

    try:

        connection = ConnectHandler(**device)

        print("Connection successful")

        return connection

    except Exception as e:

        print("Connection error:", e)

        return None
