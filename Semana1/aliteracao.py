from sys import stdin

for l in stdin:
    wordsInLine = l.lower().split()
    count = 0
    letter = wordsInLine[0][0]
    counted = False

    for i in range(1, len(wordsInLine)):
        if wordsInLine[i][0] == letter:
            if not counted:
                counted = True
                count += 1
        else:
            letter = wordsInLine[i][0]
            counted = False

    print(count)            
