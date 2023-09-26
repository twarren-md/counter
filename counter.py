# Start value input
while True:
    a4_start_value_input = input('Enter a start value (Default: 0): ')

    if not a4_start_value_input:
        a4_start_value = 0
        break

    try:
        a4_start_value = int(a4_start_value_input)
        break

    except ValueError:
        print ("Invalid entry.", end=" ")

# End value input
while True:
    a4_end_value_input = input('Enter an end number: ')

    try:
        a4_end_value = int(a4_end_value_input)
        if a4_end_value <= a4_start_value:
            print ("Invalid entry. End value must be greater than the start value.")
        else:
            break

    except ValueError:
        print ("Invalid entry.", end=" ")

# Step value input
while True:
    a4_step_value_input = input('Enter a step value (Default: 1): ')

    if not a4_step_value_input:
        a4_step_value = 1
        break

    try:
        a4_step_value = int(a4_step_value_input)
        if a4_step_value > (a4_end_value - a4_start_value):
            print ("Invalid entry. Step value must be no greater than the difference between the start value and the end value.")
        elif a4_step_value < 1:
            print ("Invalid entry. Step value must not be less than 1.")
        else:
            break

    except ValueError:
        print ("Invalid entry.", end=" ")

a4_end_value = a4_end_value + 1
print('The numbers are: ')

for x in range(a4_start_value, a4_end_value, a4_step_value):
    print (x, end=" ")

print(' ')
#print (f'{a4_start_value}')
#print (f'{a4_end_value}')
#print (f'{a4_step_value}')
