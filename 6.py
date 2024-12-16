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

lines = [s for s in lines.strip().split("\n")]
# lines = lines.strip().split('\n')
# lines = lines.strip().split()
lines = np.array([[el for el in line] for line in lines])
yn = len(lines)
xn = len(lines[0])
print(lines.size)
print(yn, xn)

dirs = [  # N, E, S, W ## y, x
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]
els = ["^", ">", "v", "<"]
print(dirs.index((1, 0)))

start = next((y, x) for y, s in enumerate(lines) for x, el in enumerate(s) if el in els)


def next_dir(dir):
    return dirs[(dirs.index(dir) + 1) % len(dirs)]


assert next_dir((0, -1)) == (-1, 0)  # git


def next_pos(pos, dir):
    return pos[0] + dir[0], pos[1] + dir[1]


def dir_id(dir):
    return dirs.index(dir)


ch = lines[start]
if ch not in els:
    print("wrong position")
dir = dirs[els.index(ch)]


def advance(map, pos, dir):
    while True:
        tpos = next_pos(pos, dir)
        if tpos[0] < 0 or tpos[0] >= yn or tpos[1] < 0 or tpos[1] >= xn:
            return False, False
        elif map[tpos] == "#":
            dir = next_dir(dir)
        else:
            pos = tpos
            map[pos] = "X"
            return pos, dir


pos = start
map = lines.copy()
while True:
    pos, dir = advance(map, pos, dir)
    if not pos:
        break
print(lines)
print(lines[lines == "X"].size)

res = 0
for y in range(yn):
    for x in range(xn):
        pos = start
        ch = lines[start]
        dir = dirs[els.index(ch)]
        yn = len(lines)
        xn = len(lines[0])

        map = lines.copy()  # making a copy
        map[y][x] = "#"

        id = 0
        while True:
            pos, dir = advance(map, pos, dir)
            if not pos:
                break
            if id > 16900:
                res += 1
                break
            id += 1
        print(y, x)
print(res)
print(lines.shape)
