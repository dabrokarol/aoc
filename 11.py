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

# lines = [list(s) for s in lines.strip().split('\n')]
t = np.array(lines.split())
print(t)


def update(t):
    t2 = []
    for a in t:
        if int(a) == 0:
            t2.append(1)
        elif len(str(a)) % 2 == 0:
            a = str(a)
            l = len(a)
            t2.append(int(a[: l // 2]))
            t2.append(int(a[l // 2 :]))
        else:
            a = int(a)
            t2.append(a * 2024)
    # print(t2)
    return np.array(t2)


epochs = 25
for i in range(epochs):
    t = update(t)
    # print(i,t.size)
    # print(t)

# print(t)
print(t.size)

saved = {}


def re(el, epochs):
    if type(el) != int:
        # print(el, epochs, 'wrong type')
        el = int(el)
    if epochs == 0:
        saved[el, 0] = 1

    if saved.get((el, epochs), -1) != -1:
        return saved[el, epochs]
    # print(el, epochs)

    if el == 0:
        saved[el, epochs] = re(1, epochs - 1)
    elif len(str(el)) % 2 == 0:
        l = len(str(el))
        saved[el, epochs] = re(int(str(el)[: l // 2]), epochs - 1) + re(
            int(str(el)[l // 2 :]), epochs - 1
        )
    else:
        saved[el, epochs] = re(el * 2024, epochs - 1)

    # print('\t', el, epochs)
    # print('\t','\t', saved[el, epochs])
    return saved[el, epochs]


sum = 0
t = np.array(lines.split())
for a in t:
    sum += re(int(a), 75)
print(sum)
