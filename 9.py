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

t = np.array([int(l) for l in lines])
print(t)

# position, id
t2 = np.zeros(t.size * 20)
pos = 0
id = 0
non_empty_indexes = []

for i in range(0, t.size):
    if i % 2:
        # startpos, how many numbers, id
        for j in range(t[i]):
            t2[pos + j] = -1
    else:
        for j in range(t[i]):
            t2[pos + j] = id
            non_empty_indexes.append(pos + j)
        id += 1
    pos += t[i]

for i in range(t2.size):
    if t2[i] == -1:
        id2 = non_empty_indexes.pop()
        if id2 < i:
            break
        t2[i] = t2[id2]
        t2[id2] = -1
print(t2[: t.size])


def checksum(t):
    res = 0
    for i in range(t.size):
        if t[i] != -1:
            res += i * t[i]
    return res


print(checksum(t2))

id_spaces = {}
empty_spaces = []

pos = 0
id = 0
for i in range(t.size):
    if i % 2:
        # [start, end)
        empty_spaces.append((pos, pos + t[i]))
    else:
        # [start, end)
        id_spaces[id] = (pos, pos + t[i])
        id += 1
    pos += t[i]
print(id_spaces)


for i in range(id - 1, 0 - 1, -1):
    size = id_spaces[i][1] - id_spaces[i][0]
    is1 = id_spaces[i]
    for j, es in enumerate(empty_spaces):
        if es[1] > is1[0]:
            break
        if es[1] - es[0] >= size:
            # print('id', i, is1)
            # print('emptyspace', es)
            # print('new id', (es[0], es[0]+size))
            # print('new emptyspace', (es[0]+size, es[1]))
            id_spaces[i] = (es[0], es[0] + size)
            if es[1] - es[0] > size:
                empty_spaces[j] = (es[0] + size, es[1])
            else:
                empty_spaces.remove(es)
            break
res = 0
for i in range(id - 1, 0 - 1, -1):
    is1 = id_spaces[i]
    for j in range(is1[0], is1[1]):
        res += i * j

print(id_spaces)

print(res)
