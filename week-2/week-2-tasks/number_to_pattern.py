user_input = int(input("Give a number: "))

prt = []
for i in range(1, user_input+1):
    if i % 2 != 0:
      prt.append('%')
    else:
       prt.append('#')

print("".join(prt))  