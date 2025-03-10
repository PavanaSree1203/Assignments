student_data = {
    101: "Alice",
    102: "Bob",
    103: "Charlie",
    104: "David",
    105: "Eve"
}

# 1.1 Adding a value
student_data[106] = "Frank"

# 1.2 Updating a value
student_data[101] = "Alice Smith"

# 1.3 Accessing a value
print(student_data[103])

# 1.4 Nested dictionary
classes = {
    "classA": {1: "Alice", 2: "Bob"},
    "classB": {3: "Charlie", 4: "David"}
}

# 1.5 Accessing nested value
print(classes["classA"][2])

# 1.6 Printing keys
print(list(student_data.keys()))

# 1.7 Deleting a value
del student_data[102]
print(student_data)