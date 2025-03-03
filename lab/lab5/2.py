import re

def match_string(s):
    pattern = r"ab{2,3}$" 
    return bool(re.fullmatch(pattern, s))

user_input = input()

if match_string(user_input):
    print("The string matches the pattern")
else:
    print("The string does not match the pattern")
