'''
6. Write a function in python to find the sum of the cube of elements in a list.
The list is received as an argument to the function, in turn the function must
return the sum. Write the main function which invokes the above function.
'''

def find_cube(lst):
    sum = 0
    for i in lst:
        sum += i**3
    print(sum)

a = [1, 2, 3]
find_cube(a) # 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36
