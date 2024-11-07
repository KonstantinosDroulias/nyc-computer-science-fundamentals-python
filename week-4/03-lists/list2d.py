data = [
    [4, 12, 56],
    [7, 23, 44],
    [3, 78, 98],
    [5, 12, 46]
]

print(data[2][1])

for i in range(len(data)):
    for j in range(len(data[i])):
        print(data[i][j], end=' ')
    print()