character = input("enter character")
vowels = ['a','e','i','o','u','A','E','I','O','U']
if character in vowels:
    print("{} is vowel".format(character))
else:
    print("{} is not vowel ".format(character))
