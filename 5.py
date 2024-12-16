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
    while True:
        line = input().strip()
        if line == "":
            break
        lines += "\n" + line

# lines = [s.split() for s in lines.strip().split('\n')]
lines = lines.strip().split("\n")
# lines = lines.strip().split()
v = {}
# count = 0
# def getname(a):
#     global count
#     global v
#     if a not in v:
#         count += 1
#         v[a] = count
#     return v[a]
G = {}

for line in lines:
    if "|" in line:
        a, b = line.split("|")
        a = int(a)
        b = int(b)

        G[a] = G.get(a, [])
        G[b] = G.get(b, [])
        G[a].append(b)


ord = []
res = 0
res2 = 0
for line in lines:
    if "," in line:
        s = set()
        flag = True
        t = [int(a) for a in line.split(",")]
        for v in t:
            s.add(v)
            for w in G[v]:
                if w in s:
                    flag = False
                    break
        if flag:
            res += t[len(t) // 2]
        else:
            l = []
            for v in t:
                i = len(l) - 1
                last = len(l)
                while i >= 0:
                    if l[i] in G[v]:
                        last = i
                    i -= 1
                l.insert(last, v)
            res2 += l[len(l) // 2]


print(res)
print(res2)
