import re

def snake_to_camel(snake_str):
    words = snake_str.split('_')  
    camel_case_str = words[0].lower() + ''.join(word.capitalize() for word in words[1:])
    return camel_case_str

user_input = input()

camel_case_result = snake_to_camel(user_input)
print(camel_case_result)
