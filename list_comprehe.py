"""

doubling by using a for loop
"""

integers = [2,8,16,40,80,800]

double = []
for i in integers:
    double.append(i*2)
print(double)

print("-----------")
"""
doubling by list comprehension
"""

double1 = [i*2 for i in integers]  # basically the same as for loop but in one line

print(double1)


print("-----------")


"""
squre nums , only even 

"""
integers1 = [1,2,3,4,5,6,7,8,9,10]

sqr = []

for i in integers1:
    if(i ** 2) % 2 == 0:
        sqr.append(i**2)
print(sqr)

# list comprehension

sqr1 = [i**2 for i in integers1 if (i **2 )% 2 == 0]

print(sqr1)