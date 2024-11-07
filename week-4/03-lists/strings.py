
s ="This is a string!"

c = input("Type a character: ")

counter = 0
lower_s = s.lower()
lower_c = c.lower()
for i in range(len(s)):
    if lower_s[i] == lower_c:
        counter += 1
print(f"{c} found {counter} times")