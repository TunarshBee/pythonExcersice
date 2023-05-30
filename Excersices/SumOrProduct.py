print("Please provide two non-negative number")
num1 = int(input("Enter the first num: "))
while num1 < 1:
    num1 = int(input("Enter a number greater than zero: "))
num2 = int(input("Enter the second number: "))
while num2 < 1:
    num2 = int(input("Enter a number greater than zero : "))
if num2 & num1:
    result = num1 * num2
    if result < 1000:
        print("The result is:{}".format(result))
    else:
        sumResult = num1 + num2
        print("The result is:{}".format(sumResult))