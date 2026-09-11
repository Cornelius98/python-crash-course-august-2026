import numpy

#Addition operator (+)
num_1 = 100
num_2 = 200
sum = num_1 + num_2 + num_1
print("Sum: ", sum)

#Substraction (-)
sub_1 = 500
sub_2 = 200
difference = sub_1 - sub_2
print("Difference: ", difference)

#multiplication (*)
multi_1 = 10
multi_2 = 50
product = multi_1 * multi_2 * 10
print("Product: ", product)

#Division (/)
numarator = 250
denominator = 55
quotient = numarator / denominator
print("Quotient is: ", quotient)

#Remainder (% - Modulus sign)
r_1 = 1
r_2 = 2
remainder = r_1 % r_2
print("Remainder is: ", remainder)

#Power (or index)
result = pow(2, 3)
result_2 = 2**3
print("2 Power 3 result: ", result_2)


#Floor division(//)
floor_1 = 10
floor_2 = 3
r_floor = floor_1 // floor_2
print("Floor Division: ", r_floor)


#More complex math calculation
angle = 45
cos_45 = numpy.cos(angle)
print("Cos 45: ", numpy.deg2rad(cos_45))