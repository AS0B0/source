sws = [60, 65, 55, 70, 65]
dbs = [55, 50, 55, 65, 70]
oss = [60, 75, 50, 70, 60]

number = 0
for number in range(len(sws)):
    sw = sws[number]
    db = dbs[number]
    os = oss[number]

    total = sw + db + os
    ave = total / 3

    if  sw < 40 or db < 40 or os < 40 or ave < 60:
        print("%d번 학생 불합격." % (number + 1))
    else:
        print("%d번 학생 합격."% (number + 1))
