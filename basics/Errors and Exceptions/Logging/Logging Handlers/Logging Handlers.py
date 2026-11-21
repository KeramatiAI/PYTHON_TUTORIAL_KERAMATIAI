"""
Logging Handlers
Logging handlers in Python determine where and how log messages are processed and outputted. They play an important role in directing log messages to specific destinations such as the console, files, email, databases, or even remote servers.


Each handler can be configured independently to control the format, log level, and other properties of the messages it processes.

Types of Logging Handlers
Following are the various types of logging handlers in Python −

StreamHandler − Sends log messages to streams such as sys.stdout or sys.stderr. Useful for displaying log messages in the console or command line interface.

FileHandler − Writes log messages to a specified file on the file system. Useful for persistent logging and archiving of log data.

RotatingFileHandler − Similar to FileHandler but automatically rotates log files based on size or time intervals. Helps manage log file sizes and prevent them from growing too large.

SMTPHandler − Sends log messages as emails to designated recipients via SMTP. Useful for alerting administrators or developers about critical issues.

SysLogHandler − Sends log messages to the system log on Unix-like systems (e.g., syslog). Allows integration with system-wide logging facilities.

MemoryHandler − Buffers log messages in memory and sends them to a target handler after reaching a certain buffer size or timeout. Useful for batching and managing bursts of log messages.

HTTPHandler − Sends log messages to a web server via HTTP or HTTPS. Enables logging messages to a remote server or logging service.
"""