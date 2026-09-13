class MyClass:
    def __init__(self):
        self.__private_var = "I am Private"

    def __private_method(self):
        return "This is a private method"

    def show_private(self):
        return self.__private_var + " and " + self.__private_method()

obj = MyClass()
print(obj.show_private())    # ✓ Access through method
# print(obj.__private_method())  # ✗ AttributeError
print(obj._MyClass__private_method())  # ✓ Access using name mangling