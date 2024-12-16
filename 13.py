import numpy as np


def parse_input(file_name="in2"):
    try:
        with open(file_name, "r") as f:
            lines = f.read().strip()
    except FileNotFoundError:
        print("File not found. Enter grid manually (empty line to finish):")
        lines = ""
        while True:
            line = input().strip()
            if line == "":
                break
            lines += "\n" + line

    if not lines.strip():
        raise ValueError("Input is empty.")

    rows = lines.split("\n\n")
    return np.array(rows)


rows = parse_input("in")
COST_A = 3
COST_B = 1
CONV = 10000000000000


def solve(X, Y, A, B) -> int:
    A = np.array(A, dtype=int)
    B = np.array(B, dtype=int)
    X = int(X)
    Y = int(Y)
    pos = np.array((X, Y))
    # print(A, B, pos)
    minimum = np.inf
    # a1, b1 = np.linalg.solve(np.array([A, B]).T, pos)
    # print("1", a1*COST_A + b1*COST_B)
    for i in range(101):
        for j in range(101):
            if np.all(A * i + B * j == pos):
                # print(pos)
                minimum = min(minimum, i * COST_A + j * COST_B)
    return int(minimum) if minimum != np.inf else 0


def are_dependent(A, B) -> bool:
    return np.linalg.matrix_rank(np.array([A, B])) == 1


assert are_dependent((1, 1), (2, 2)) == 1
assert are_dependent((1, 1), (2, 3)) == 0


def solve2(X, Y, A, B) -> int:
    A = np.array(A, dtype="int")
    B = np.array(B, dtype="int")
    X = int(X) + CONV
    Y = int(Y) + CONV
    print(A, B, X, Y)
    pos = np.array((X, Y))

    a1, b1 = np.linalg.solve(np.array([A, B]).T, np.array(pos))

    a1 = np.round(a1, 3)
    b1 = np.round(b1, 3)
    print(a1, b1)

    if a1.is_integer() and b1.is_integer():
        print(a1, b1, np.round(a1), np.round(b1))
        return np.round(a1) * COST_A + np.round(b1) * COST_B
    # if is_near_int(a1) and is_near_int(b1):
    return 0


res = 0
res2 = 0
for rs in rows:
    rss = rs.split("\n")
    Ax = rss[0].split(":")[1].split(",")[0].split("+")[1]
    Ay = rss[0].split(":")[1].split(",")[1].split("+")[1]
    Bx = rss[1].split(":")[1].split(",")[0].split("+")[1]
    By = rss[1].split(":")[1].split(",")[1].split("+")[1]
    X = rss[2].split(":")[1].split(",")[0].split("=")[1]
    Y = rss[2].split(":")[1].split(",")[1].split("=")[1]

    # print(Ax, Ay, Bx, By, X, Y)
    # print(solve(X, Y, (Ax, Ay), (Bx, By)))
    # res = solve(X, Y, (Ax, Ay), (Bx, By))
    res2 += solve2(X, Y, (Ax, Ay), (Bx, By))
    # print(solve2(X, Y, (Ax, Ay), (Bx, By)))
    # res2 += solve2(X, Y, (Ax, Ay), (Bx, By))

print(res)
print(res2)

# print("""[26 66] [67 21] 10000000012748 10000000012176
# 118679050709.0 103199174542.00002""")
# print(26*118679050709 + 67*103199174542.00002)
# print(66*118679050709 + 21*103199174542.00002)
