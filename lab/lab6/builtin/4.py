import math
import time

def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000) 
    return math.sqrt(number)

number = int(input("Enter a number: "))
delay_ms = int(input("Enter delay in milliseconds: "))

result = delayed_sqrt(number, delay_ms)
print(f"Square root of {number} after {delay_ms} milliseconds is {result}")
