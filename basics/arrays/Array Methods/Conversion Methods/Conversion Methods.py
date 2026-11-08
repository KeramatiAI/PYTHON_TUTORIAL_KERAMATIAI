"""
Conversion Methods
These methods are used to convert arrays to and from bytes, files, lists, and Unicode strings.

Sr.No.	Methods with Description
1
frombytes(buffer)

Appends items from the bytes-like object, interpreting its content as an array of machine values.

2
tobytes()

Converts the array to a bytes representation.

3
fromfile(f, n)

Reads n items from the file object f and appends them to the array.

4
tofile(f)

Writes all items to the file object f.

5
fromlist(list)

Appends items from the list to the array.

6
tolist()

Converts the array to a list with the same items.

7
fromunicode(s)

Extends the array with data from the given Unicode string. The array must have type code 'u'.

8
tounicode()

Converts the array to a Unicode string. The array must have type code 'u'.
"""