import csv # Found documentetion here https://www.geeksforgeeks.org/working-csv-files-python/

username = input("Type your username: ")
pin = input("Type your pin: ")

filename = "users.csv"

fields = []
rows = []

flag = False

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    next(csvreader)

    for row in csvreader:
        if row[0] == username and row[1] == pin:
            flag = True
            print("Access Granted!!!")
            break 

if not flag:
    print("Username or PIN are incorrect...")