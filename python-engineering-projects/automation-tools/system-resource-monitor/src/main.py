import psutil

def monitor():

    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent

    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")

if __name__ == "__main__":
    monitor()
