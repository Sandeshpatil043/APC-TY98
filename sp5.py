# exp5
char = input("Enter a character: ").lower()

if len(char) == 1 and char.isalpha():
    if char in "aeiou":
        print(f"'{char}' is a Vowel.")
    else:
        print(f"'{char}' is a Consonant.")
else:
    print("Invalid input! Please enter a single alphabetic character.")