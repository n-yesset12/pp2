def count_lines(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            line_count = sum(1 for _ in file)
        print(f"Total number of lines: {line_count}")
    except FileNotFoundError:
        print("File not found. Please check the filename and path.")
    except PermissionError:
        print("Permission denied. Cannot access the file.")

file_path = input()

count_lines(file_path)
