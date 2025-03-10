try:
    with open("nonexistent_file.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("FileNotFoundError: The specified file does not exist.")