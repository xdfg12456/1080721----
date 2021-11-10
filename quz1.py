from sys import stdin


for line in stdin:
    in_data = {}
    count = 0
    line = line.replace("[", "").replace("]", "").split(",")
    for n in line:
        count += 1
        try:
            in_data[int(n)] += 1
        except:
            in_data[int(n)] = 1

    goal = count/2

    for i in in_data.items():
        if(i[1] > goal):
            print(i[0])
