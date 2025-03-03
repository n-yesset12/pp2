def is_palindrome(s):
    return s == s[::-1]  

user_input = input()

if is_palindrome(user_input):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
