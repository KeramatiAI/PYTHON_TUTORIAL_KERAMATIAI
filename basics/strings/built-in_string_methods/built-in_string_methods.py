"""
1	capitalize()
Capitalizes first letter of string.

2	casefold()
Converts all uppercase letters in string to lowercase. Similar to lower(), but works on UNICODE characters alos.

3	center(width, fillchar)
Returns a space-padded string with the original string centered to a total of width columns.

4	count(str, beg= 0,end=len(string))
Counts how many times str occurs in string or in a substring of string if starting index beg and ending index end are given.

5	decode(encoding='UTF-8',errors='strict')
Decodes the string using the codec registered for encoding. encoding defaults to the default string encoding.

6	encode(encoding='UTF-8',errors='strict')
Returns encoded string version of string; on error, default is to raise a ValueError unless errors is given with 'ignore' or 'replace'.

7	endswith(suffix, beg=0, end=len(string))
Determines if string or a substring of string (if starting index beg and ending index end are given) ends with suffix; returns true if so and false otherwise.

8	expandtabs(tabsize=8)
Expands tabs in string to multiple spaces; defaults to 8 spaces per tab if tabsize not provided.

9	find(str, beg=0 end=len(string))
Determine if str occurs in string or in a substring of string if starting index beg and ending index end are given returns index if found and -1 otherwise.

10	format(*args, **kwargs)
This method is used to format the current string value.

11	format_map(mapping)
This method is also use to format the current string the only difference is it uses a mapping object.

12	index(str, beg=0, end=len(string))
Same as find(), but raises an exception if str not found.

13	isalnum()
Returns true if string has at least 1 character and all characters are alphanumeric and false otherwise.

14	isalpha()
Returns true if string has at least 1 character and all characters are alphabetic and false otherwise.

15	isascii()
Returns True is all the characters in the string are from the ASCII character set.

16	isdecimal()
Returns true if a unicode string contains only decimal characters and false otherwise.

17	isdigit()
Returns true if string contains only digits and false otherwise.

18	isidentifier()
Checks whether the string is a valid Python identifier.

19	islower()
Returns true if string has at least 1 cased character and all cased characters are in lowercase and false otherwise.

20	isnumeric()
Returns true if a unicode string contains only numeric characters and false otherwise.

21	isprintable()
Checks whether all the characters in the string are printable.

22	isspace()
Returns true if string contains only whitespace characters and false otherwise.

23	istitle()
Returns true if string is properly "titlecased" and false otherwise.

24	isupper()
Returns true if string has at least one cased character and all cased characters are in uppercase and false otherwise.

25	join(seq)
Merges (concatenates) the string representations of elements in sequence seq into a string, with separator string.

26	ljust(width[, fillchar])
Returns a space-padded string with the original string left-justified to a total of width columns.

27	lower()
Converts all uppercase letters in string to lowercase.

28	lstrip()
Removes all leading white space in string.

29	maketrans()
Returns a translation table to be used in translate function.

30	partition()
Splits the string in three string tuple at the first occurrence of separator.

31	removeprefix()
Returns a string after removing the prefix string.

32	removesuffix()
Returns a string after removing the suffix string.

33	replace(old, new [, max])
Replaces all occurrences of old in string with new or at most max occurrences if max given.

34	rfind(str, beg=0,end=len(string))
Same as find(), but search backwards in string.

35	rindex( str, beg=0, end=len(string))
Same as index(), but search backwards in string.

36	rjust(width,[, fillchar])
Returns a space-padded string with the original string right-justified to a total of width columns.

37	rpartition()
Splits the string in three string tuple at the ladt occurrence of separator.

38	rsplit()
Splits the string from the end and returns a list of substrings.

39	rstrip()
Removes all trailing whitespace of string.

40	split(str="", num=string.count(str))
Splits string according to delimiter str (space if not provided) and returns list of substrings; split into at most num substrings if given.

41	splitlines( num=string.count('\n'))
Splits string at all (or num) NEWLINEs and returns a list of each line with NEWLINEs removed.

42	startswith(str, beg=0,end=len(string))
Determines if string or a substring of string (if starting index beg and ending index end are given) starts with substring str; returns true if so and false otherwise.

43	strip([chars])
Performs both lstrip() and rstrip() on string.

44	swapcase()
Inverts case for all letters in string.

45	title()
Returns "titlecased" version of string, that is, all words begin with uppercase and the rest are lowercase.

46	translate(table, deletechars="")
Translates string according to translation table str(256 chars), removing those in the del string.

47	upper()
Converts lowercase letters in string to uppercase.

48	zfill (width)
Returns original string leftpadded with zeros to a total of width characters; intended for numbers, zfill() retains any sign given (less one zero).
"""