start = int(input("Give Start Point: "))
end = int(input("Give Start Point: "))

"""
# Range begins from 0 to x
for i in range(10):
    print(i)
"""

if start <= end:
    for i in range(start, end + 1):
        print(i)
else:
    for i in range(start, end - 1, -1):
        print(i)