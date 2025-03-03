import re

def replace_characters(s):
    pattern = r"[ ,.]"  
    replaced_string = re.sub(pattern, ":", s)
    return replaced_string


user_input = input()


result = replace_characters(user_input)
print(result)
