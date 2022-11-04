file1 = open("calendar2.txt", "w")
with open('calendar1.txt', 'r') as f:
    cnt = 1
    for line in f:
        if cnt <= 16:
            print(line, end='', file=open("calendar2.txt", "a"))
            cnt += 1
        else:
            break
file1.close()

#debugging:
print(__file__)