"""
Using Direct Indexing
In this approach, we access values in a nested dictionary by specifying each key in a sequence of square brackets. Each key in the sequence refers to a level in the nested dictionary, progressing one level deeper with each key −
"""
# Define a nested dictionary
students = {
    "Alice": {"age": 21, "major": "Computer Science"},
    "Bob": {"age": 20, "major": "Engineering"},
    "Charlie": {"age": 22, "major": "Mathematics"}
}

# Access Alice's major
alice_major = students["Alice"]["major"]
print("Alice's major:", alice_major)

# Access Bob's age
bob_age = students["Bob"]["age"]
print("Bob's age:", bob_age)
"""
Following is the output of the above code −

Alice's major: Computer Science
Bob's age: 20
"""