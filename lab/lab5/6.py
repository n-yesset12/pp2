import re

def replace_characters(s):
    pattern = r"[ ,.]"  
    replaced_string = re.sub(pattern, ":", s)
    return replaced_string


user_input = input("Enter a string: ")


result = replace_characters(user_input)
print("Modified string:", result)
