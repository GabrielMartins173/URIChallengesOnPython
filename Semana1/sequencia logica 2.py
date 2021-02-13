userInp = input()
listInp =  userInp.split()
inp = int(listInp[0])
inp2 = int(listInp[1])
line = []
count = 0

for i in range(1, (inp2//inp)+1):
    for j in range(1, inp+1):
        count += 1
        line.append(count)

    for k in range(len(line)):

        if(k == (len(line) - 1)):
            print("{}".format(line[k]))

        else:
            print("{} ".format(line[k]), end = '')
    
    line.clear()