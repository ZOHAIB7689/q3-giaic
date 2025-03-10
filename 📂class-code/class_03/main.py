#String

# basics of strings

# The 'r' prefix before the string indicates a raw string literal, which means backslashes are treated as literal characters instead of escape characters.
# The backslashes in the string are not performing any escape sequences, they are simply part of the string.
raw_string = r"Hello \t,\n Worl\\d"
print(raw_string)

# tripple Quotes

tripple_quotes = '''Hello

world '''
print(tripple_quotes)

# Performing Differrent Operations on String Object

my_string = 'Hello, ' + 'World!'
my_string = 'Hello, World!'; print(my_string[0]) # prints 'H'
my_string = 'Hello, World!'; print(my_string[7:]) # prints 'World!'
my_string = 'Hello, World!'; print(len(my_string)) # prints 13
my_string = 'Hello, World!'; print(my_string.upper()) # prints 'HELLO, WORLD!'
my_string = 'Hello, World!'; print(my_string.lower()) # prints 'hello, world!'



# The split() method splits a string into a list where each word is a list item.
# It splits at each space character by default.
# Example:
my_string = 'Hello, World! This is a test.'
split_string = my_string.split()
print(split_string)  # Output: ['Hello,', 'World!', 'This', 'is', 'a', 'test.']

# You can also specify a separator to split the string.
# Example:
my_string = 'Hello, World! This is a test.'
split_string = my_string.split(',')
print(split_string)  # Output: ['Hello', ' World! This is a test.']

# The join() method is a string method that returns a string concatenated with the elements of an iterable.
# It takes an iterable (like a list or tuple) as an argument and concatenates all the elements in the iterable into a single string.
# The string on which the join() method is called is inserted between each element in the iterable.
# Example:
my_list = ['Hello', 'World', 'This', 'is', 'a', 'test']
joined_string = ' '.join(my_list)
print(joined_string)  # Output: 'Hello World This is a test'

# The join() method can be used with different separators. For example, to join elements with a comma and a space:
my_list = ['Hello', 'World', 'This', 'is', 'a', 'test']
joined_string = ', '.join(my_list)
print(joined_string)  # Output: 'Hello, World, This, is, a, test'

# The join() method can also be used to concatenate elements of a list with a newline character for each element:
my_list = ['Hello', 'World', 'This', 'is', 'a', 'test']
joined_string = '\n'.join(my_list)
print(joined_string)  # Output: 'Hello\nWorld\nThis\nis\na\ntest'


# Other String Methods

# The strip() method removes leading and trailing characters (space is default)
# Example:
my_string = '   Hello, World!   '
stripped_string = my_string.strip()
print(stripped_string)  # Output: 'Hello, World!'

# The lstrip() method removes leading characters (space is default)
# Example:
my_string = '   Hello, World!   '
lstripped_string = my_string.lstrip()
print(lstripped_string)  # Output: 'Hello, World!   '

# The rstrip() method removes trailing characters (space is default)
# Example:
my_string = '   Hello, World!   '
rstripped_string = my_string.rstrip()
print(rstripped_string)  # Output: '   Hello, World!'

# The replace() method replaces a specified phrase with another specified phrase.
# Example:
my_string = 'Hello, World!'
replaced_string = my_string.replace('World', 'Universe')
print(replaced_string)  # Output: 'Hello, Universe!'

# The find() method finds the first occurrence of the specified value.
# Example:
my_string = 'Hello, World!'
index = my_string.find('World')
print(index)  # Output: 7

# The index() method finds the first occurrence of the specified value.
# Example:
my_string = 'Hello, World!'
index = my_string.index('World')
print(index)  # Output: 7

# The count() method returns the number of occurrences of a specified value.
# Example:
my_string = 'Hello, World! Hello, Universe!'
count = my_string.count('Hello')
print(count)  # Output: 2

# The startswith() method returns True if the string starts with the specified value.
# Example:
my_string = 'Hello, World!'
startswith_result = my_string.startswith('Hello')
print(startswith_result)  # Output: True

# The endswith() method returns True if the string ends with the specified value.
# Example:
my_string = 'Hello, World!'
endswith_result = my_string.endswith('World!')
print(endswith_result)  # Output: True
