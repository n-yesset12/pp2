def solve(numheads, numlegs):
    y = (numlegs - 2 * numheads) // 2
    x = numheads - y
    
    if x < 0 or y < 0 or 2*x + 4*y != numlegs:
        return "No valid solution"
    
    return f"Chickens: {x}, Rabbits: {y}"