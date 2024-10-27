user_input = int(input("Type a demical number to convert to binary: "))

def to_binary(n):
    #your code here

    remainder = [n % 2]
    while n // 2 != 0:
        n = n // 2
        remainder.append(n % 2)

    return remainder

output_list = to_binary(user_input)
#print (output_list)

for i in output_list.reverse():
    print(i)
