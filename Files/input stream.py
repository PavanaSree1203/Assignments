def write_to_txt(filename, text):
    """Writes text to a .txt file."""
    with open(filename, 'w') as file:
        file.write(text)

# Example usage:
text_to_write = "Hello, world!\nThis is a test."
write_to_txt("my_file.txt", text_to_write)