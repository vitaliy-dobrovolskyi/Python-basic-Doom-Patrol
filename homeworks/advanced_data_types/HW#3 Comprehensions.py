#
# Comprehensions:
# (1)
# lst = []
# for num in range(10):
#     if num % 2 == 1:
#         lst.append(num ** 2)
#     else:
#         lst.append(num ** 4)
# print(lst)
#
# (2)
# list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
#
# 12. Convert (1) to list comprehension

# lst_comp = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
# print(lst_comp)

# 13. Convert (2) to regular for with if-else

# lst=[]
# for num in range (10):
#     if num % 2==0:
#         lst.append(num // 2)
#     else:
#         lst.append (num**4)
# print(lst)

# (3)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
# print(d)
#
#
# (4)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
#     else:
#         d[num] = num // 0.5
# print(d)
#
# (5)
# dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
# print (dict_comprehension)
#
# (6)
# dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
# print(dict_comprehension)
#
# 14. Convert (3) to dict comprehension.

# dc_with_if = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
# # print(dc_with_if)


# 15*. Convert (4) to dict comprehension.

# dc_with_elif={num:num**2 if num % 2==1 else num//0.5 for num in range (1,11)}
# print(dc_with_elif)

# 16. Convert (5) to regular for with if.
#
# x = {}
# for num in range (10):
#     if num**3 % 4 == 0:
#         x[num]=num**3
# print (x)
#
# 17*. Convert (6) to regular for with if-else.

# x = {}
# for num in range(10):
#     if num ** 3 % 4 == 0:
#         x[num] = num ** 3
#     else:
#         x[num] = num
# print(x)


