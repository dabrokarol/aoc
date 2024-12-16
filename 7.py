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


def ope(a, b, op):
    if op == 1:
        return a + b
    elif op == 0:
        return a * b
    elif op == 2:
        return int(str(a) + str(b))
    else:
        print("wrong op")
        exit()


res = 0
for line in lines:
    val = line.split(":")[0]
    nums = line.split(":")[1].split()
    # print(val, nums)
    for mask in range(2 ** (len(nums) - 1)):  # all bitwise masks
        test = int(nums[0])
        for j in range(len(nums) - 1):
            op = (2**j & mask) > 0
            # print(mask, j, op)
            test = ope(test, int(nums[j + 1]), op)
            # print(op, sep=' ')
        if test == int(val):
            res += int(val)
            break
        # print()
print(res)


def findop(mask, pos):
    if pos == 0:
        return mask % 3
    print("pos, mask", pos, mask)
    print(3 ** (pos))
    print(mask // (3 ** (pos)))
    op = (mask // (3 ** (pos))) % (3)
    return op


print(findop(2, 0))
assert findop(2, 0) == 2
print(findop(9, 2))
assert (findop(9, 2)) == 1
assert (findop(18, 2)) == 2


res = 0
for line in lines:
    val = line.split(":")[0]
    nums = line.split(":")[1].split()
    # print(val, nums)
    for mask in range(3 ** (len(nums) - 1)):  # all bitwise masks
        test = int(nums[0])
        for j in range(len(nums) - 1):
            op = (mask // (3 ** (j))) % (3)
            # print(mask, j, op)
            test = ope(test, int(nums[j + 1]), op)
            # print(op, sep=' ')
        if test == int(val):
            res += int(val)
            break
        # print()
print(res)
