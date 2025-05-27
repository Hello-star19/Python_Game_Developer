
word = input("Please enter a statement: ").lower()

vowels = {"a" : 0, "e" : 0,  "i" : 0, "o" : 0, "u" : 0}

for i in word:
    if i in vowels:
        vowels[i] += 1
print(vowels)