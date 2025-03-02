import re

def camel_to_snake(camel_str):
    pattern = r"([a-z])([A-Z])" 
    snake_case_str = re.sub(pattern, r"\1_\2", camel_str).lower()  
    return snake_case_str


user_input = input("Enter a camelCase or PascalCase string: ")

snake_case_result = camel_to_snake(user_input)
print("Snake case string:", snake_case_result)
