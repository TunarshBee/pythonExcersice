word = input("Enter a word and see the ones at even positions: ")
for i in range(len(word)):
    if i % 2 != 0:
        continue
    else:
        print( word[i])

"""
The test string/word is "pynative"
And the expected output is "p n t v"
"""