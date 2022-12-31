print("Zadanie z palindromami")

def isPalindrome(word):
    return word == word[::-1]
 
word = input("podaj slowo:")
reverse = isPalindrome(word)
 
if reverse:
    print("Tak to palindrom")
else:
    print("Nie, to nie palindrom")

isPalindrome(word)