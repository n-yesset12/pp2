import os

def check_path(path):
    if os.path.exists(path):
        print("The path exists.")
        
        directory = os.path.dirname(path)
        print(f"Directory portion: {directory}")

        filename = os.path.basename(path)
        print(f"Filename portion: {filename}")
    else:
        print("The path does not exist.")

user_path = input()

check_path(user_path)
