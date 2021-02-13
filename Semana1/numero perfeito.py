inp = input()
numberOfTestCases = int(inp)
inpList = []

for l in range(numberOfTestCases):
    newInp = input()
    inpList.append(newInp)

divisors = []

for i in range(1, len(inpList)+1):

    sum = 0
    number = int(inpList[i-1])

    for j in range(1, number):
        if(number % j == 0):
            divisors.append(j)

    for k in range(len(divisors)):
        sum += divisors[k]

    if sum == number:
        print("{} eh perfeito".format(number))
    else:
        print("{} nao eh perfeito".format(number))
    
    divisors.clear()