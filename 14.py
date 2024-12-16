import numpy as np


def read_file(file_name="14.in"):
    try:
        with open(file_name, "r") as f:
            lines = f.read().strip()
    except FileNotFoundError:
        print("File not found. Enter input manually (empty line to finish):")
        lines = ""
        while True:
            line = input().strip()
            if line == "":
                break
            lines += "\n" + line
    if not lines.strip():
        raise ValueError("Input is empty.")
    return lines.split("\n")


def parse_input(filename):
    lines = read_file(filename)
    arr = np.zeros(len(lines), dtype=DT)
    for i, line in enumerate(lines):
        pos = line.split(" ")[0].split("=")[1].split(",")
        v = line.split(" ")[1].split("=")[1].split(",")
        arr[i]["pos"] = pos
        arr[i]["v"] = v
    return arr


def print_out_map(arr, t=0):
    grid = np.zeros((Y, X), dtype=int)
    print(f"time: {t}###############################################")
    print(grid.shape)
    for el in arr:
        # el being (x, y) and map being indexed as (y, x)
        grid[tuple(el["pos"][::-1])] += 1
    for i in range(Y):
        for j in range(X):
            num = grid[(i, j)]
            print(("#" if num else "."), end="", flush=False)
        print()
    print(flush=True)


def quadrant(pos):
    if pos[0] < X // 2 and pos[1] < Y // 2:
        return 1
    elif pos[0] > X // 2 and pos[1] < Y // 2:
        return 2
    elif pos[0] < X // 2 and pos[1] > Y // 2:
        return 3
    elif pos[0] > X // 2 and pos[1] > Y // 2:
        return 4
    else:
        return 0


def write_out_grid(arr, t, filename):
    grid = np.zeros((Y, X), dtype=int)
    for el in arr:
        # again reversing element so that coordinates are (y, x)
        grid[tuple(el["pos"][::-1])] += 1
    with open(filename, "a") as f:
        f.write(f"time: {t}###############################################\n")
        for i in range(Y):
            for j in range(X):
                num = grid[(i, j)]
                f.write(("#" if num else "."))
            f.write("\n")
        f.write("\n")


DT = [("pos", "2int"), ("v", "2int")]
X = 101
Y = 103
# X = 11
# Y = 7


def solve1():
    arr = parse_input("in/14.in")
    boundary = np.array((X, Y), dtype="2int")

    epochs = 100
    for t in range(epochs):
        for j in range(len(arr)):
            arr[j]["pos"] += arr[j]["v"]
            arr[j]["pos"] %= boundary

    quadrants_sum = [0, 0, 0, 0, 0]

    for i in range(len(arr)):
        quadrants_sum[quadrant(arr[i]["pos"])] += 1

    print(quadrants_sum[1:])
    print(np.prod(quadrants_sum[1:]))


def solve2():
    arr = parse_input("in/14.in")
    boundary = np.array((X, Y), dtype="2int")
    t = 0

    while t < 10000:
        t += 1
        for j in range(len(arr)):
            arr[j]["pos"] += arr[j]["v"]
            arr[j]["pos"] %= boundary
        write_out_grid(arr, t, "result")
        print(t)


if __name__ == "__main__":
    solve1()
    solve2()
