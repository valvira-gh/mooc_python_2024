# Typical errors

Here is a selection of typical errors you will likely come across, along with some situations where they may occur.

### ValueError

This error is often thrown when the argument passed to a function is somehow invalid. For example, the function call float("1,23")causes an error, because decimals are always separated by a point in Python, and here we have a comma.

### TypeError

This error occurs when a value is of the wrong type. For example, the function call len(10) causes a TypeError, because the function len requires a value whose length can be calculated, such as a string or a list.

### IndexError

This common error occurs when trying to refer to an index which doesn't exist. For example, the expression "abc"[5] causes an IndexError, because the string in question has no index 5.

### ZeroDivisionError

As the name implies, this error is thrown when trying to divide by zero, which we know from mathematics to always be a bad idea. For example, if we try to determine the arithmetic mean of values in a list with the formula sum(my_list) / len(my_list), but our list has length zero, this error will occur.

Exceptions in file handling

Some common errors when working with files are FileNotFoundError (when trying to access a file which doesn't exist), io.UnsupportedOperation (when trying to perform an operation on a file which is not supported by the mode in which the file is opened) or PermissionError (the program lacks necessary permissions to access the file).