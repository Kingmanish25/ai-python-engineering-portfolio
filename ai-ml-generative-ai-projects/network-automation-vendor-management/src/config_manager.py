def push_configuration(connection, vendor):

    print("Applying configuration...")

    if vendor == "cisco":

        commands = [
            "interface loopback0",
            "description Automation-Test",
            "ip address 10.10.10.1 255.255.255.255"
        ]

    elif vendor == "juniper":

        commands = [
            "set interfaces lo0 unit 0 family inet address 10.10.10.1/32"
        ]

    else:

        print("Unsupported vendor")
        return

    output = connection.send_config_set(commands)

    print(output)
