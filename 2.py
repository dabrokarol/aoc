def checkline(line):
    if line[1] - line[0] > 0:
        decreasing = 1
    else:
        decreasing = -1
    works = True
    for i in range(1, len(line)):
        # print((line[i] - line[i-1])*decreasing)
        a = (line[i] - line[i - 1]) * decreasing
        if a <= 0 or a > 3:
            works = False
    return works


res = 0
while True:
    line = input().strip()
    if line == "":
        break
    line = [int(a) for a in line.split()]
    for i in range(len(line)):
        if checkline(line[:i] + line[i + 1 :]):
            res += 1
            break
print(res)
