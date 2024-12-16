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

lines = [[int(el) for el in s] for s in lines.strip().split("\n")]

# [print(' '.join(l)) for l in lines]

t = np.array(lines)
print(t)

l = [(1, 0), (-1, 0), (0, -1), (0, 1)]


def dfs(pos):
    # global vis
    # global saved
    if saved.get(pos, -1) != -1:
        return saved[pos]
    vis[pos] = True
    if t[pos] == 9:
        saved[pos] = 1, 1
        return saved[pos]
    score = 0
    rating = 0
    for dy, dx in l:
        pos2 = pos[0] + dy, pos[1] + dx
        if pos2[0] < 0 or pos2[1] < 0 or pos2[0] >= t.shape[0] or pos2[1] >= t.shape[1]:
            continue
        if t[pos2] != t[pos] + 1:
            continue
        if vis.get(pos2, False):
            rating += saved[pos2][1]
            continue
        returned = dfs(pos2)
        score += returned[0]
        rating += returned[1]
    saved[pos] = score, rating
    return saved[pos]


res1 = 0
res2 = 0
for y in range(t.shape[0]):
    for x in range(t.shape[1]):
        if t[y][x] == 0:
            vis = {}
            saved = {}
            returned = dfs((y, x))
            print((y, x))
            print(returned[0])
            print(returned[1])
            res1 += returned[0]
            res2 += returned[1]

print(res1, res2)
print((t == 9).sum())
