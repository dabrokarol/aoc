import numpy as np

try:
    with open("in", "r", encoding="utf-8") as f:
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

t = np.array(lines)

dir = ((1, 0), (0, 1), (-1, 0), (0, -1))


def previous_dir(dir):
    if dir == (1, 0):
        return (0, -1)
    if dir == (1, 0):
        return (1, 0)
    if dir == (-1, 0):
        return (0, 1)
    if dir == (0, -1):
        return (-1, 0)


def next_dir(dir):
    if dir == (1, 0):
        return (0, 1)
    if dir == (0, 1):
        return (-1, 0)
    if dir == (-1, 0):
        return (0, -1)
    if dir == (0, -1):
        return (1, 0)


visited = set()


def dfs(pos):
    if pos in visited:
        return 0, 0
    visited.add(pos)

    chr = t[pos]
    area = 1
    perimeter = 0
    for d in dir:
        newpos = tuple(np.add(pos, d))
        if (
            newpos[0] < 0
            or newpos[1] < 0
            or newpos[0] >= t.shape[0]
            or newpos[1] >= t.shape[1]
        ):
            perimeter += 1
            continue
        if t[newpos] == chr:
            area, perimeter = np.add(dfs(newpos), (area, perimeter))
        else:
            perimeter += 1
    return area, perimeter


visited_2 = set()
sides = {}


def dfs2(pos):
    if pos in visited_2:
        return sides[pos], (0, 0)
    visited_2.add(pos)

    chr = t[pos]
    area = 1
    perimeter = 0
    temp_sides = set()
    for d in dir:
        newpos = tuple(np.add(pos, d))
        if (
            newpos[0] < 0
            or newpos[1] < 0
            or newpos[0] >= t.shape[0]
            or newpos[1] >= t.shape[1]
        ):
            temp_sides.add(d)
            perimeter += 1
        elif t[newpos] != chr:
            temp_sides.add(d)
            perimeter += 1
    sides[pos] = temp_sides
    print(chr, pos, sides[pos])
    for d in dir:
        newpos = tuple(np.add(pos, d))
        if d in sides[pos]:
            continue
        if t[newpos] == chr:
            ss, (a, p) = dfs2(newpos)
            for s in ss:
                if s in sides[pos]:
                    perimeter -= 0.5
            area, perimeter = np.add((a, p), (area, perimeter))

    return sides[pos], (area, perimeter)


result = 0
result_2 = 0

for y in range(t.shape[0]):
    for x in range(t.shape[1]):
        if (y, x) not in visited:
            area, perimeter = dfs((y, x))
            result += area * perimeter
            print(t[y][x], area, perimeter)
            area, perimeter = dfs2((y, x))[1]
            result_2 += area * perimeter
            print(t[y][x], area, perimeter)

print(t)
print(result)
print(result_2)
