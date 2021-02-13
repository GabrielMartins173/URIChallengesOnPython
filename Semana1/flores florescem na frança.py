from sys import stdin

for l in stdin:
    wordsInLine = l.lower().split()
    valid = -1
    letter = wordsInLine[0][0]

    if letter == '*':
        break

    for i in range(1, len(wordsInLine)):

        if wordsInLine[i][0] == letter:
            valid = 1
        
        elif wordsInLine[i][0] != letter:
            valid = 0

    if(valid == 0):
        print("N")
    elif(valid == 1):
        print("Y")