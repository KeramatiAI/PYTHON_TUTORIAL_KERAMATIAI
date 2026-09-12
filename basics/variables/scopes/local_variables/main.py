# Local Variables
######################################################################################
# #Type 1
# def get_information(first_name,last_name,age,salary,weight,height):
#    information = f"information is: {first_name},{last_name},{age},{salary},{weight},{height}"
#    return information
#
# print(get_information("Davoud", "Keramati",20,50000000,80.250,182.50))
#######################################################################################
# Type 2
first_name = "Abbas" # Global Variable
last_name = "Salari" # Global Variable
age = 50 # Global Variable
salary = 250000000 # Global Variable
weight = 70.50 # Global Variable
height = 175.350 # Global Variable

def get_information():
    first_name = "Davoud" # Local Variable
    last_name = "Keramati" # Local Variable
    age = 20 # Local Variable
    salary = 100000000 # Local Variable
    weight = 79.500 # Local Variable
    height = 180.25 # Local Variable
    return f"{first_name},{last_name},{age},{salary},{weight},{height}"


print(get_information())
print(f"{first_name},{last_name},{age},{salary},{weight},{height}")

