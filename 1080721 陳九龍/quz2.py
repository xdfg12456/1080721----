from sys import stdin

for line in stdin:
    sum = 0
    line = line.replace("[", "").replace("]", "").split(",")
    for n in line:
        sum ^= int(n)
    print(sum)
