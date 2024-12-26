import pandas as pd

file = open('cities.csv')
lines = file.readlines()

states = {}

for i in range(1, len(lines)):
    line = lines[i]
    elements = line.split(',')
    
    if len(elements) > 1:    
        #print(elements)
        state = elements[-1].strip()
        city = elements[-2].strip() # remove all spaces and \n -> the .strip()
        city = city[1:-2] # take only the city without the ""
    
        if state in states:
            states[state].append(city)
        else:
            states[state] = [city]
    
search = input("Search State: ")
if search in states:
    print(states[search])
else:
    print(f"State {search} not found")