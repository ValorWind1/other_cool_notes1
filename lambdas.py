"""
lamnbdas : they dont need a name or id(identifier).
******use for functions that are only used once *****
ex : such as maps , filters etc.
"""

integers = [1,2,3,4,5,6]

"""
doing it normal way by a function  
"""
# def square(n):
#     return n*n
#
# print(list(map(square,integers)))




# doing the same but using a lambda since we are only using it once

# lambda n: n * n

print(list(map(lambda n:n*n ,integers)))
