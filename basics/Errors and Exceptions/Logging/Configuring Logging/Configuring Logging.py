"""Configuring Logging
Configuring logging in Python refers to setting up various components such as loggers, handlers, and formatters to control how and where log messages are stored and displayed. This configuration allows developers to customize logging behavior according to their application's requirements and deployment environment.

Example
In the following example, the getLogger() function retrieves or creates a named logger. Loggers are organized hierarchically based on their names. Then, handlers like "StreamHandler" (console handler) are created to define where log messages go. They can be configured with specific log levels and formatters.

The formatters specify the layout of log records, determining how log messages appear when printed or stored −
"""
import logging

# Create logger
logger = logging.getLogger('my_app')
logger.setLevel(logging.DEBUG)  # Set global log level

# Create console handler and set level to debug
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Add console handler to logger
logger.addHandler(console_handler)

# Example usage
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
"""The result produced is as shown below −

2024-06-19 09:05:20,852 - my_app - DEBUG - This is a debug message
2024-06-19 09:05:20,852 - my_app - INFO - This is an info message
2024-06-19 09:05:20,852 - my_app - WARNING - This is a warning message
2024-06-19 09:05:20,852 - my_app - ERROR - This is an error message
2024-06-19 09:05:20,852 - my_app - CRITICAL - This is a critical message"""