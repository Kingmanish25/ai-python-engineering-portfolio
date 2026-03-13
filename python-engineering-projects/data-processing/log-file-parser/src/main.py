def parse_log(file):

    with open(file) as f:
        for line in f:
            if "ERROR" in line:
                print(line)

parse_log("server.log")
