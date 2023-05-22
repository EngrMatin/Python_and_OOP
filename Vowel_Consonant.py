letter = input("Enter a letter: ")

if (letter >='a' and letter <='z') or (letter >='A' and letter <='Z'):
    if letter =='a' or letter=='A' or letter=='e' or letter=='E' or letter=='i' or letter=='I' or letter=='o' or letter=='O' or letter=='u' or letter=='U':
        print("\n It is a Vowel.")
    else:
        print("\n It is a Consonant.")
else:
    print("\n It is not a character in the alphabet.")