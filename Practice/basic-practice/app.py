# print(+False)
# print(2+True)
# age = 20
# if age > 19:
#   print("Hello")
#   print("d")
# print("Check")

# my_list_1: int = [1, 2, 3, "Java", 3.14, True] #Type hinting is not enforced in python, but you should mention appropriate data type in this case 'list'
# my_list: list = [1, 2, 3, "Python", 3.14, 3+2j]

# print(type(my_list_1), " my_list_1 = ", my_list_1)  # <class 'list'>
# print(type(my_list), " my_list   =  " + str(my_list)) # we will look into type casting in classes ahead

# my_list = [1,2] #mutable
# my_tuple = (1,2) #immutable
# print(type(my_list))
# print(type(my_tuple))

# range = range(1,10,20)
# print(type(range), "range = ", range.step)

# string methods

# multiline string
msg = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

msg = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
# print(msg[6])

# one line string
text_double = "Hell'o, Python"
text_double = "Hell""o, Python"
text_double = "Hell" \
"o, Python"
# print(text_double)

# Accessing string characters
# print("Character at index 1:", text_double[1]) # Output: e


text = "Hell", "o Python"
# print(text) # now it's tuple

# list
my_list_1: int = [1, 2, 3, "Java", 3.14, True]
# print(my_list_1[3][1])

# tuple
my_tuple = (1, "AI", 2.71, [1, 2, 3])
# print("\nTuple Example:", my_tuple)
# Modifying a list inside a tuple
my_tuple[3].append(4)
# print("Modified Tuple with List:", my_tuple)  # The list inside the tuple is mutable

# for i in range(1,6,2):
#     print(i) #1,3,5

# for i in range(1,6,1):
#     print(i) #1,2,3,4,5

# for i in range(1,6,3):
#     print(i) #1,4

my_set = {1, 4, 111, "Ibad"}
my_set: frozenset = frozenset({1, 4, 111, "Ibad",False,True,2233,3,"3"})
my_set: frozenset = frozenset([1, 4, 111, "Ibad"])
# print(type(my_set), "my_set = ", my_set)


# string methods
string = "iBad ur rehman"
# string_method = string.casefold()
# string_method = string.capitalize()
# string_method = string.center(30,"i")
# string_method = string.center(30,)
# string_method = string.count("a")
# string_method = string.encode()
# print(string_method)
# print(type(string_method))
# string_method = string.endswith("n")
# string_method = string.find("ur")
# txt = "For only {price:.2f} dollars!"
# print(txt.format(price=56.2222))
# string_method = string.index("z") # it shows error 
string2 = "python developer "
# string_method = string2.split("e") # ['python d', 'v', 'lop', 'r']
# join_string = "e".join(string_method) # python developer
# string_method = "e" in string2
# string_method = "a" not in string2
# string_method = string2.__len__()
# string_method = string2 + " " + "hun"
# string_method = string2[0:6] # slicing, last param is exclusive, output: python
# string_method = string2.upper()
# string_method = string2.lower()
# string_method = string2.replace("python","typescript")
string_method = string2 * 5
print(string_method)


# list methods
