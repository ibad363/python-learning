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

my_list = [1,2] #mutable
my_tuple = (1,2) #immutable
print(type(my_list))
print(type(my_tuple))

range = range(1,10,20)
print(type(range), "range = ", range.step)