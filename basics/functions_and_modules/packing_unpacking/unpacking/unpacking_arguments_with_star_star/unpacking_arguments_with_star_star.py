def unpack_kwargs(name, family, age, city):
    print("Unpacked keyword arguments:", name, family, age, city)


# Dictionary of values to unpack
info = {"name": "Davoud", "family": "Keramati", "age": 25, "city": "Los Angeles"}

# Calling the function with unpacked values
unpack_kwargs(**info)
