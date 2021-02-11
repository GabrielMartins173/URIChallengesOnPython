def split(word): 
    return list(word) 

e = input()
entries = split(e)
numberOfBits = len(entries)

numberOfOnes = 0

for entry in range(numberOfBits):

    if(int(entries[entry]) == 1):
        numberOfOnes += 1

if (numberOfOnes % 2 == 0):
    e = e + '0'
else:
    e = e + '1'

print(e)