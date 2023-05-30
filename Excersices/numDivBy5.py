numbers = [15,10,34,45,23,45,57,25,35,70,85]
print("Ginven numbers: {}".format(numbers))
print("Divisible by 5:")
for number in numbers:
    if number % 5 == 0:
        print(number)