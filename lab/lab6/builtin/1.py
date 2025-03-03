import math

def multiply_list(numbers):
    return math.prod(numbers)

user_input = input()
numbers = list(map(int, user_input.split()))

result = multiply_list(numbers)
print(result)
