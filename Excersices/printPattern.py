num = int(input("Enter the amount of rows you will like to have in number: "))
for row in range(1,num+1):
    for col in range(row):
        print(row, end="")
    print("")


"""
Same solution with while loop

num = int(input("Enter the amount of rows you will like to have in number: "))
counter = 0
while counter < num:
    counter += 1
    for i in range(counter):
        print(counter, end="")
    print("")
"""