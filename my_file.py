# '''binary search'''
# def binary_search(input_array, value):
#     """Your code goes here."""
#     l,h = 0, len(input_array)-1
#
#     while l <= h:
#         mid = (h+l)//2
#         if input_array[mid] == value:
#             return mid
#         elif value > input_array[mid]:
#             l = mid+1
#         else:
#             h = mid-1
#     return -1
#
# test_list = [1,3,9,11,15,19,29]
# test_val1 = 25
# test_val2 = 15
#
# a = binary_search(test_list, test_val1)
# b = binary_search(test_list, test_val2)
# print(b)
#
#
#
#
# """Implement a function recursively to get the desired
# Fibonacci sequence value.
# Your code should have the same input/output as the
# iterative code in the instructions."""
#
# def get_fib(position):
#     l = [0]
#     while len(l)-1<=position:
#         if len(l)-1 == position:
#             return l[-1]
#         elif len(l) == 1:
#             l.append(1)
#         else:
#             a = l[len(l)-1]+l[len(l)-2]
#             l.append(a)
#
# # Test cases
# print(get_fib(9))
# print(get_fib(11))
# print(get_fib(0))
#
# #************************************************** using recursive technique  **********************************************#
# def get_fib(position):
#     if position == 0 or position == 1:
#         return position
#     return get_fib(position - 1) + get_fib(position - 2)
#
# print(get_fib(9))
# # print get_fib(11)
# # print get_fib(0)
