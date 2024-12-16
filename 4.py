import numpy as np

try:
    with open("in", "r") as f:
        lines = f.read().strip()
except FileNotFoundError:
    print("file not found")
    lines = ""

if lines == "":
    while True:
        line = input().strip()
        if line == "":
            break
        lines += "\n" + line

# lines = [s.split() for s in lines.strip().split('\n')]
# lines = lines.strip().split('\n')
# lines = lines.strip().split()

t = np.array([[s for s in line] for line in lines.strip().split()])
pattern = "XMAS"


def countline(line, p):
    count = 0
    for i in range(len(line) - len(p) + 1):
        flag = True
        for j in range(len(p)):
            if line[i + j] != p[j]:
                flag = False
                break
        if flag:
            count += 1
    return count


res = 0
for y in range(t.shape[0]):
    line = t[y, :]
    res += countline(line, pattern)
    res += countline(line[::-1], pattern)
print(res)
for x in range(t.shape[1]):
    line = t[:, x]
    res += countline(line, pattern)
    res += countline(line[::-1], pattern)
print(res)

m = min(t.shape)
for d in range(-m, m):
    xs = np.arange(0, t.shape[1])
    ys = xs + d
    ids = np.logical_and(ys >= 0, ys < t.shape[0])
    xs = xs[ids]
    ys = ys[ids]
    line = t[ys, xs]
    res += countline(line, pattern)
    res += countline(line[::-1], pattern)
for d in range(m * 2):
    xs = np.arange(0, t.shape[1])
    ys = -1 * xs + d
    ids = np.logical_and(ys >= 0, ys < t.shape[0])
    xs = xs[ids]
    ys = ys[ids]
    line = t[ys, xs]
    res += countline(line, pattern)
    res += countline(line[::-1], pattern)

print(res)


possible = [
    ["M*M", "*A*", "S*S"],
    ["S*M", "*A*", "S*M"],
    ["M*S", "*A*", "M*S"],
    ["S*S", "*A*", "M*M"],
]
count = 0
for p in possible:
    for y in range(t.shape[0] - 3 + 1):
        for x in range(t.shape[1] - 3 + 1):
            flag = True
            for i in range(3):
                for j in range(3):
                    if p[i][j] != "*" and p[i][j] != t[y + i][x + j]:
                        flag = False
            if flag:
                count += 1
print(count)
