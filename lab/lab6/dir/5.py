def write_list_to_file(filename, data_list):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for item in data_list:
                file.write(str(item) + '\n') 
        print(f"List has been written to {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

my_list = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

file_path = input()

write_list_to_file(file_path, my_list)
