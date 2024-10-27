user_input = input("Type a binary positive number to convert to demical: ")

def to_demical(n):
    #your code here
    demical_sum = 0
    power = int(len(n))
    
        
    #while power >= 0:
    for i in n:
        power = power - 1
        #print(f'Power {power}')
        number = int(i)
        #print(f'Number {number}')
        number_cal = number * 2**power
        #print( f'Nc {number_cal}')
        demical_sum = demical_sum + number_cal


    return demical_sum

demical = to_demical(user_input)
print(demical)