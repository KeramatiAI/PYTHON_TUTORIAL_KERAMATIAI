"""
Python raises a KeyError if the key given inside the square brackets is not present in the dictionary object −
"""
capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
print ("Captial of Haryana is : ", capitals['Haryana'])
"""
Following is the error obtained −

   print ("Captial of Haryana is : ", capitals['Haryana'])
                                      ~~~~~~~~^^^^^^^^^^^
KeyError: 'Haryana'
"""