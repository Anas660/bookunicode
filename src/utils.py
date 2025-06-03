def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def log_message(message):
    print(f"[LOG] {message}")