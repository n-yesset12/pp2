import string

def generate_text_files():
    for letter in string.ascii_uppercase: 
        filename = f"{letter}.txt"
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(f"This is file {filename}\n") 
            print(f"Created: {filename}")
        except Exception as e:
            print(f"Error creating {filename}: {e}")

generate_text_files()
