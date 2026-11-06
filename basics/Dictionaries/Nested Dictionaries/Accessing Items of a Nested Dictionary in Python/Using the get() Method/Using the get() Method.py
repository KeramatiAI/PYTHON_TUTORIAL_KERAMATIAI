"""
Using the get() Method
The get() method is used to fetch the value associated with the specified key. If the key does not exist, it returns a default value (which is None if not specified) −
"""
# Define a nested dictionary
students = {
    "Alice": {"age": 21, "major": "Computer Science"},
    "Bob": {"age": 20, "major": "Engineering"},
    "Charlie": {"age": 22, "major": "Mathematics"}
}

# Access Alice's major using .get()
alice_major = students.get("Alice", {}).get("major", "Not Found")
print("Alice's major:", alice_major)

# Safely access a non-existing key using .get()
dave_major = students.get("Dave", {}).get("major", "Not Found")
print("Dave's major:", dave_major)
"""
Output of the above code is as follows −

Alice's major: Computer Science
Dave's major: Not Found
"""