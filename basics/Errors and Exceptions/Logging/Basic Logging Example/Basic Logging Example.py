"""Basic Logging Example
Following is a basic logging example in Python to demonstrate its usage and functionality −
"""
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Example usage
def calculate_sum(a, b):
   logging.debug(f"Calculating sum of {a} and {b}")
   result = a + b
   logging.info(f"Sum calculated successfully: {result}")
   return result

# Main program
if __name__ == "__main__":
   logging.info("Starting the program")
   result = calculate_sum(10, 20)
   logging.info("Program completed")
"""Output
Following is the output of the above code −

2024-06-19 09:00:06,774 - INFO - Starting the program
2024-06-19 09:00:06,774 - DEBUG - Calculating sum of 10 and 20
2024-06-19 09:00:06,774 - INFO - Sum calculated successfully: 30
2024-06-19 09:00:06,775 - INFO - Program completed"""