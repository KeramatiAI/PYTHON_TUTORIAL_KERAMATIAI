"""
Handling an Exception in Python
If you have some suspicious code that may raise an exception, you can defend your program by placing the suspicious code in a try: block. After the try: block, include an except: statement, followed by a block of code which handles the problem as elegantly as possible.

The try: block contains statements which are susceptible for exception

If exception occurs, the program jumps to the except: block.

If no exception in the try: block, the except: block is skipped.

Syntax
Here is the simple syntax of try...except...else blocks −

try:
   You do your operations here
   ......................
except ExceptionI:
   If there is ExceptionI, then execute this block.
except ExceptionII:
   If there is ExceptionII, then execute this block.
   ......................
else:
   If there is no exception then execute this block.
Here are few important points about the above-mentioned syntax −

A single try statement can have multiple except statements. This is useful when the try block contains statements that may throw different types of exceptions.

You can also provide a generic except clause, which handles any exception.

After the except clause(s), you can include an else clause. The code in the else block executes if the code in the try: block does not raise an exception.

The else block is a good place for code that does not need the try: block's protection.
"""