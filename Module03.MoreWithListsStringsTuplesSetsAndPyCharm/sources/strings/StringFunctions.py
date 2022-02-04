hello = "hello my name is Nguyen Van Loc"

# string.capitalize(): capitalizes first letter of string
hello = hello.capitalize()
print(hello)

# string.startswith(prefix) – determines if string starts with prefix
# string.endswith(suffix) – determines if string ends with suffix
print(hello.startswith("a"))
print(hello.endswith("c"))

# string.startswith(prefix) – determines if string starts with prefix
# string.endswith(suffix) – determines if string ends with suffix
print(hello.isupper())
print(hello.islower())

# string.find(str) – determines if str occurs in string
# string.index(str) – determines index of str in string
print(hello.find("name"))
print(hello.index("name"))

# string.replace(old, new) – replaces all occurrences of old in string with new
hello = hello.replace("name", "full name")
print(hello)

# string.strip() – trims whitespace from beginning and end of string

# string.upper() - returns uppercased string from given string
# string.lower() - returns lowercased string from given string
print(hello.upper())
print(hello.lower())