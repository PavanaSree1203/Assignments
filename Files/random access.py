def read_random_access(filename, position, length):
    """Reads a portion of a file at a specific position."""
    with open(filename, 'rb') as file:
        file.seek(position)
        data = file.read(length)
        print(data.decode('utf-8'))

# Example usage:
read_random_access("my_file.txt", 5, 10)