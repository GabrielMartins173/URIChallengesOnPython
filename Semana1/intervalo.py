entries = int(input())
listOfIn = []
listofOut = []

for entry in range(entries):
    entry = int(input())

    if(entry >= 10 and entry <= 20):
        listOfIn.append(entry)
    else:
        listofOut.append(entry)

print("{} in".format(len(listOfIn)))
print("{} out".format(len(listofOut)))