pattern = "mul(*,*)"
# * means any valid integer
allowed = [str(i) for i in range(10)]
print(allowed)


def searchpattern(s, p):
    enabled = getenabled(s)
    tab = []
    result = 0
    for i in range(len(s)):
        i_tmp = i
        j = 0
        found = False
        initialized = False

        numbers = []
        number = None

        # print("starting from ", i)
        while j < len(p) and i < len(s):
            # print(i,j, s[i], p[j])

            if p[j] == "*":
                if not initialized:
                    initialized = True
                    number = None
                # print('\t', number, initialized)

                if s[i] in allowed:
                    if number is not None:
                        number *= 10
                        number += int(s[i])
                    else:
                        number = int(s[i])
                    i += 1
                elif s[i] == p[j + 1] and number is not None:
                    numbers.append(number)
                    j += 1
                    initialized = False
                else:
                    break

            else:
                if s[i] != p[j]:
                    break
                if j == len(p) - 1 and s[i] == p[j]:
                    found = True
                i += 1
                j += 1

        if found:
            tab.append(s[i_tmp:i])
            if enabled[i_tmp]:
                result += numbers[0] * numbers[1]

        i = i_tmp
    return tab, result


import numpy as np


def getenabled(s):
    enabled = np.ones(len(s))
    p1 = "do()"
    p2 = "don't()"
    for i in range(len(s)):
        i_tmp = i
        flag = 1
        j = 0
        while j < len(p1):
            if i >= len(s):
                flag = 0
                break
            if s[i] != p1[j]:
                flag = 0
                break
            i += 1
            j += 1
        if flag == 1:
            enabled[i_tmp:] = 1
        flag = 1
        i = i_tmp
        j = 0
        while j < len(p2):
            if i >= len(s):
                flag = 0
                break
            if s[i] != p2[j]:
                flag = 0
                break
            i += 1
            j += 1
        if flag == 1:
            enabled[i_tmp:] = 0
        i = i_tmp
    return enabled


print(
    # searchpattern('elo*elo', 'elo'),
    # searchpattern('o123ao12a','o*a'),
    searchpattern(
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))",
        pattern,
    )
)

res = 0
s = ""
while True:
    line = input().strip()
    s += line
    if line == "":
        break
res += searchpattern(s, pattern)[1]

print(res)

# print(
#     getenabled("do()"+"a"*10+"don't()"+'a'*10+"do()"+'a'*10)
# )
