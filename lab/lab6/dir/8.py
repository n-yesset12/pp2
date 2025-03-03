import os

def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK): 
            try:
                os.remove(file_path) 
                print(f"✅ File '{file_path}' has been deleted successfully.")
            except Exception as e:
                print(f"An error occurred while deleting the file: {e}")
        else:
            print("File does not exist. Please check the file path")

file_path = input()

delete_file(file_path)
