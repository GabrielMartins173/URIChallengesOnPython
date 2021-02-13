inp = int(input())       

for i in range(1, inp+1):
    if i % 2 == 0:
        square = i * i  
        print("{}^2 = {}".format(i, square))