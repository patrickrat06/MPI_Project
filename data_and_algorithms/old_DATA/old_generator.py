import random


def generate_list_files(filename, size, stype="random"):
    if stype == "random":
        data = [random.randint(0, 10000) for _ in range(size)]
    elif stype == "sorted":
        data = sorted([random.randint(0, 10000) for _ in range(size)])

    with open(f"list_files/{filename}", "a") as f:
        f.write(", ".join(map(str, data)) + "\n")

for i in range(100001):
    generate_list_files(filename="automating_test.csv", size=20, stype="random")
#generate_test_file(filename="test.csv", size=20, stype="sorted")
