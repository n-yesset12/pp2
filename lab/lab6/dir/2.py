import os

def check_path_access(path):
    print(f"Checking access for: {path}\n")
    
    if os.path.exists(path):
        print("Path exists.")
        
        if os.access(path, os.R_OK):
            print("Path is readable.")
        else:
            print("Path is not readable.")

        if os.access(path, os.W_OK):
            print("Path is writable.")
        else:
            print("Path is not writable.")

        if os.access(path, os.X_OK):
            print("Path is executable.")
        else:
            print("Path is not executable.")
    else:
        print("Path does not exist.")

user_path = input()


check_path_access(user_path)
