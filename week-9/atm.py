
def read_accounts():
    file = open('accounts.csv', 'r')
    lines = file.readlines()
    accounts = {}
    for line in lines:
        parts = line.strip().split(',') #parts is a list 
        if parts[0] != 'id':
            account = {'id': parts[0], 'pin': parts[1], 'name': parts[2], 'balance': float(parts[3])}
            
            accounts[parts[0]] = account
            
    return accounts

def login():
    id = input('ID: ')
    pin = input("Pin: ")
    return id, pin

def check_login(id, pin, accounts):
    if id in accounts:
        account = accounts[id] #grabes the list with all the info in that specific id
        if account["pin"] == pin: #checks if the pin is correct
            return account
    return None

menu = ['Balance', 'Deposit', 'Withdraw', 'Exit']
def atm_menu():
    for index, i in enumerate(menu):
        print(f"{index + 1}. {i}")
    ch = int(input("Choose: "))
    return ch

# Load accounts
accounts = read_accounts()

def deposit(account):
    amount = float(input('Ammount: €'))
    if amount > 0:
        account['balance'] += amount
    else:
        print("Invalid amount")
        
def withdraw(account):
    amount = float(input("Amount: €"))
    if amount > 0 and amount <= account['balance']:
        account['balance'] -= amount
    else:
        print('Invalid amount')
        
def save(accounts):
    file = open('accounts.csv', 'w')
    file.write('id,pin,name,balance\n')
    for key in accounts:
        a = accounts[key]
        file.write(f"{a['id']},{a['pin']},{a['name']},{str(a['balance'])}\n")

pin = ""
id = ""
# Loop until admin gives 0000 id and 0000 pin
while pin != '0000' and id != '0000':
    
    # Display login prompt {user give id and pin}
    id, pin = login() #saves the return id and pin from the functions
    account = check_login(id, pin, accounts) 
    
    # If login ok
    if account is not None:
        print(f"Welcome, {account['name']}")   
        # Loop until user selects #
        choice = -1
        while choice != 4:
            # Display ATM menu and get user's choice
            choice = atm_menu()
            # Server User Menu
            """if choice == 1:
                pass
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            elif choice == 0:
                pass
            else:
                print("Invalid Choice")"""
            match choice:
                case 1:
                    print(f"Balance {account['balance']}")
                case 2:
                    deposit(account)
                case 3:
                    withdraw(account)
                case 4:
                    # If user choice 0: Update Account in CSV
                    save(account)
                    print("Exit...")
                case _:
                    print("Invalid Selection")
            
            