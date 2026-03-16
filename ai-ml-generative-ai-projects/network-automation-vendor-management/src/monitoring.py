
def monitor_device(connection):

    print("Running monitoring checks...")

    commands = [
        "show ip interface brief",
        "show version"
    ]

    for cmd in commands:

        output = connection.send_command(cmd)

        print("\nCommand:", cmd)
        print(output[:500])
