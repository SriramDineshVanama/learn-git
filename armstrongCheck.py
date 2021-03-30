# Check whether the input number is an Armstrong number
#Hello

# Take the input number but store it as a string for now
input_num_str = str(input('Enter the number without any leading zeroes : \n'))

# Form a list of digits
digits = list(input_num_str)

# Compute the sum of the cube of all digits one by one
sum_of_cubes = 0
for i in digits :
    sum_of_cubes = sum_of_cubes + (int(i) ** 3)

if sum_of_cubes == int(input_num_str) :
    print('Yayy, ' + input_num_str + ' is an Armstrong number')
else :
    print('Nope ' + input_num_str + ' is not an Armstrong number')
