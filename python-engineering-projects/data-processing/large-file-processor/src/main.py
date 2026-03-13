def process_large_file(file):

    with open(file) as f:

        for i, line in enumerate(f):

            if i % 1000 == 0:
                print(line.strip())

process_large_file("bigfile.txt")
