hay_point = {}

numberOfWords, numberOfDescriptions = [int(x) for x in input().split()]

while numberOfWords:
    numberOfWords -= 1
    role, salary = input().split()
    hay_point[role] = int(salary)

while numberOfDescriptions:
    numberOfDescriptions -= 1
    salary = 0
    descriptionRole = input().split()
    endPoint = input()
    for word in descriptionRole:
        try:
            salary += hay_point[word]
        except KeyError:
            continue

    print(salary)