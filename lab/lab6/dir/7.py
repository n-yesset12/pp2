import shutil

def copy_file(source, destination):
    try:
        shutil.copyfile(source, destination)
        print(f"File copied successfully from '{source}' to '{destination}'")
    except FileNotFoundError:
        print("Source file not found. Check the filename and path.")

source_file = input()
destination_file = input()

copy_file(source_file, destination_file)
