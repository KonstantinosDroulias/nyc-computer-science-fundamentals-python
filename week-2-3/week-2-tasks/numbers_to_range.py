a = int(input('Type a number for "a": '))
b = int(input('Type a number for "b": '))
c = int(input('Type a number for "c": '))

if a > b:
    for i in range(a, b-1, -c):
        print(i)
elif a == b:
    print(f"'a'{a} and 'b'{b} are equal")
else:
    for i in range(a, b+1, c):
        print(i)