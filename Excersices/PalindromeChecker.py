word = input("Enter a word to check if it is a palindrome word: ")
print("Original word:", word)
pal =""
for i in (word):
    pal = i + pal
if pal == word:
    print("Yes. given word is a palindrome word")
else:
    print("No. given word is not a palindrome word")
