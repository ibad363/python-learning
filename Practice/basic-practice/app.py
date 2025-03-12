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
text_double = "Hello," \
" Python"
# print(text_double)


# list
my_list_1: int = [1, 2, 3, "Java", 3.14, True]
# print(my_list_1[3][1])

# for i in range(1,6,2):
#     print(i) #1,3,5

# for i in range(1,6,1):
#     print(i) #1,2,3,4,5

# for i in range(1,6,3):
#     print(i) #1,4

my_set = {1, 4, 111, "Ibad"}
my_set: frozenset = frozenset({1, 4, 111, "Ibad",False,True,2233,3,"3"})
my_set: frozenset = frozenset([1, 4, 111, "Ibad"])
print(type(my_set), "my_set = ", my_set)