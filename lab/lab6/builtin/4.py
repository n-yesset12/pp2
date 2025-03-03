import math
import time

def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000) 
    return math.sqrt(number)

number = int(input())
delay_ms = int(input())

result = delayed_sqrt(number, delay_ms)
print(f"Square root of {number} after {delay_ms} milliseconds is {result}")
