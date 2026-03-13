with open("log.txt") as f:

    lines = f.readlines()

error_count = sum(1 for line in lines if "ERROR" in line)

print("Error count:", error_count)
