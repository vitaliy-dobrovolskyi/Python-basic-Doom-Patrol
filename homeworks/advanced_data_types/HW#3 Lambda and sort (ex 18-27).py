# Lambda:
#
# (7)
# def foo(x, y):
#     if x < y:
#         return x
#     else:
#         return y
#
# (8)
# foo = lambda x, y, z: z if y < x and x > z else y
#
# 18. Convert (7) to lambda function

# lmb = lambda x, y: x if x < y else y
# print(lmb(3, 6))

# 19*. Convert (8) to regular function

# def foo (x,y,z):
#     if y>x and x>z:
#         return z
#     else:
#         return y
# print (foo(6,7,5))
#
# lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
#
# 20. Sort lst_to_sort from min to max

# lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
# print(sorted (lst_to_sort))

# 21. Sort lst_to_sort from max to min

# lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
# print(sorted (lst_to_sort, reverse = True))

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2

# lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
# new_lst_to_sort = list(map(lambda x: x * 2, lst_to_sort))
# print(new_lst_to_sort)

# 23*. Raise each list number to the corresponding number on another list:

# list_A = [2, 3, 4]
# list_B = [5, 6, 7]
#
# lst = list(map(lambda x, y: x ** y, list_A, list_B))
# print(lst)

# 24. Use reduce and lambda to compute the numbers of a lst_to_sort.

# lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
# import functools
#
# foo = functools.reduce (lambda x,y: x+y, lst_to_sort)
# print (foo)

# 25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.

# lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
# new_lst = list(filter(lambda x: (x%2==1), lst_to_sort))
# print(new_lst)

# 26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.

# b = range (-10,10)
# new_lst = list (filter(lambda b:b<0, range(-10,10)))
# print(new_lst)

# 27*. Using the filter function, find the values that are common to the two lists:
# list_1 = [1, 2, 3, 5, 7, 9]
# list_2 = [2, 3, 5, 6, 7, 8]
#
# common_lst = list (filter (lambda x: x in list_1, list_2))
# print(common_lst)
