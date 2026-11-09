"""
Writing to a File Using writelines() Method
The writelines() method is used to write a list of strings to a file. Each string in the list is written to the file sequentially without adding any newline characters automatically.

Example
In this example, we are creating a list of strings, lines, with each string ending in a newline character. We then open a file "example.txt" in write mode and use the writelines() method to write all the strings in the list to the file in one operation −
"""
# List of lines to write to the file
lines = ["First line\n", "Second line\n", "Third line\n"]

# Open a file in write mode
with open("example.txt", "w") as file:
    file.writelines(lines)

print ("File opened successfully!!")
"""
The output obtained is as shown below −

File opened successfully!!
"""