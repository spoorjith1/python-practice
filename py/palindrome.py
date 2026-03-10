def is_palindrome(str):
    str = str.lower().replace(" ", "")
    return str == str[::-1]

word = input("Enter a word : ")
if is_palindrome(word):
    print("palindrome")
else:
    print("--- Not palindrome ---")
