N = int(input())
def square_generator(N):
    for i in range(N + 1):
        yield i ** 2

for square in square_generator(N):
    print(square)