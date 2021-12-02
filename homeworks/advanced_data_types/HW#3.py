# 1. Define the id of next variables:
# int_a = 55
# print(id(int_a))
#
# str_b = 'cursor'
# print(id(str_b))
#
# set_c = {1, 2, 3}
# print(id(set_c))
#
# lst_d = [1, 2, 3]
# print(id(lst_d))
#
# dict_e = {'a': 1, 'b': 2, 'c': 3}
# print(id(dict_e))
#
# 2. Append 4 and 5 to the lst_d and define the id one more time.
# lst_d = [1, 2, 3]
# lst_d.append([4,5])
# print(lst_d, id(lst_d))

# 3. Define the type of each object from step 1.

# int_a = 55
# print (type(int_a))
#
# str_b = 'cursor'
# # print(type(str_b))
# #
# set_c = {1, 2, 3}
# # print(type(set_c))
# #
# lst_d = [1, 2, 3]
# # print(type(lst_d))
# #
# dict_e = {'a': 1, 'b': 2, 'c': 3}
# print(type(dict_e))

# 4*. Check the type of the objects by using isinstance.

# print(isinstance(int_a, int))
# print(isinstance(str_b, str))
# print(isinstance(set_c, set))
# print(isinstance(lst_d, list))
# print(type(dict_e) is dict)

# String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."
#
# 5. With .format and curly braces {}

# print ("Anna has {} apples and {} peaches.".format (3,7))

# 6. By passing index numbers into the curly braces.

# print("Anna has 3 {1} and 7 {0}.".format("apples", "peaches"))

# 7. By using keyword arguments into the curly braces.

# print("Anna has 3 {first} and 7 {second}.".format(first="apples", second="peaches"))

# 8*. With indicators of field size (5 chars for the first and 3 for the second)

# print("Anna has {0:4} apples and 7 {1:2}.".format(3, "peaches"))

# 9. With f-strings and variables

# a = "apples"
# b = 7
# print(f"Anna has 3 {a} and {b} peaches.")

# 10. With % operator
# peaches = 7
# apples = 3
# print("Anna has %d apples and %d peaches." %(apples, peaches))

# 11*. With variable substitutions by name (hint: by using dict)
# name1 = "apples"
# num2 = 7
# data_dict = {"name":name1, "num":num2}
# print("Anna has 3 %(name)s and %(num)d peaches." % data_dict)


