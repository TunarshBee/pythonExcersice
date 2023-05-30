word = input("Enter the word to be used: ")
num = int(input("enter the amount of character you want to remove: "))
while num >= len(word):
    num = int(input("enter a number less than the word you provided: "))
print(word[num:])
