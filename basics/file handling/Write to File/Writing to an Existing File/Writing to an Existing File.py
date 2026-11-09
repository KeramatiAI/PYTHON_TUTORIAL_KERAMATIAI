"""
Writing to an Existing File
When an existing file is opened in write mode ('w'), its previous contents are erased. Opening a file with write permission treats it as a new file. To add data to an existing file without erasing its contents, you should open the file in append mode ('a').

Example
The following example demonstrates how to open a file in append mode and add new text to it −
"""
# Open a file in append mode
fo = open("foo.txt", "a")
text = "TutorialsPoint has a fabulous Python tutorial"
fo.write(text)

# Close opened file
fo.close()
"""
If you open this file with any text editor application such as Notepad, it will have the following content −

Python is a great language.
Yeah its great!!
TutorialsPoint has a fabulous Python tutorial
"""