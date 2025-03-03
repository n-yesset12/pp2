import os

def list_contents(path):
    try:
        all_items = os.listdir(path)

        directories = [d for d in all_items if os.path.isdir(os.path.join(path, d))]
        files = [f for f in all_items if os.path.isfile(os.path.join(path, f))]

        print("\nDirectories:")
        print(directories)

        print("\nFiles:")
        print(files)

        print("\nAll Directories and Files:")
        print(all_items)

    except FileNotFoundError:
        print("The specified path does not exist.")


user_path = input()

list_contents(user_path)
