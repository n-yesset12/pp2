import re

def insert_spaces(s):
    pattern = r"([a-z])([A-Z])"  
    spaced_string = re.sub(pattern, r"\1 \2", s)
    return spaced_string

user_input = input()

result = insert_spaces(user_input)
print("String with spaces:", result)
