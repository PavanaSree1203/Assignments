def read_file_stream(filename):
    """Reads and prints the contents of a file stream."""
    with open(filename, 'r') as file:
        for line in file:
            print(line, end='')

# Example usage:
read_file_stream("my_file.txt")