def read_from_index(filename, index, num_bytes):
    with open(filename, 'rb') as file:
        file.seek(index)
        data = file.read(num_bytes)
        print(data.decode('utf-8', errors='ignore'))

read_from_index("my_file.txt", 10, 5)