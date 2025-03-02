import re

def match_string(s):
    pattern = r"^a.*b$"  
    return bool(re.fullmatch(pattern, s))

user_input = input("Enter a string: ")


if match_string(user_input):
    print("The string matches the pattern.")
else:
    print("The string does NOT match the pattern.")
