import numpy as np

try:
    with open("in2", "r") as f:
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

lines = [list(s) for s in lines.strip().split("\n")]
lines = np.array(lines)
# lines = lines.strip().split('\n')

chrs = []
for i in range(ord("a"), ord("z") + 1):
    chrs.append(chr(i))
for i in range(ord("A"), ord("Z") + 1):
    chrs.append(chr(i))
for i in range(ord("0"), ord("9") + 1):
    chrs.append(chr(i))
# print(chrs)
occ = {}
for y, l in enumerate(lines):
    for x, a in enumerate(l):
        if a in chrs:
            occ[a] = occ.get(a, [])
            occ[a].append((y, x))


def get_pos(p1, p2):
    y1, x1 = p1
    y2, x2 = p2
    dy, dx = y1 - y2, x1 - x2
    pos = []
    for i in range(1000):
        pos1 = y1 + i * dy, x1 + i * dx
        pos2 = y2 - i * dy, x2 - i * dx
        pos.append(pos1)
        pos.append(pos2)
    return pos


result = 0
for key in occ.keys():
    # print(key)
    tmp = list(occ[key])
    for i in range(len(tmp)):
        for j in range(i + 1, len(tmp)):
            v1 = tmp[i]
            v2 = tmp[j]
            print(v1, v2)
            pos = get_pos(v1, v2)
            for p in pos:
                if (
                    p[0] < 0
                    or p[1] < 0
                    or p[0] >= lines.shape[0]
                    or p[1] >= lines.shape[1]
                ):
                    continue
                result += 1
                lines[p] = "#"

[print(" ".join(l)) for l in lines]
print((lines == "#").sum())
print(result)
