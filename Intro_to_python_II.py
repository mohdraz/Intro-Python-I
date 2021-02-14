# def mult2(x,y):
#     print(f"{x} is being multiipied by {y} ")
#     return x * y

# print(mult2(2, 7))
# a=12
# print(mult2(a, 6))

# # integer
# def foo(x):
#     print(x)
#     x = 12
#     print(x)


# a = 8
# foo(a)
# print(a)

# # string is not mutable
# def foo(x):
#     print(x)
#     x = x.upper()
#     print(x)


# a = 'hello'
# foo(a)
# print(a)

# # list is mutable which is getting mutated in the function
# def foo(x):
#     a[2] = 99

# a = [1, 2, 3, 4]
# foo(a)

# print(a[2])


# Return the centered average of an array of positive or negative ints, which we wills ay is the mean average of the values, except ignoring ht elargst and smalled values in the array. the array can be out of order. The array will have at least 3 numbers. Use integer division to compute the average

# centered_average([1, 2, 3, 4, 1000]) -> 3
# centered_average([1, 1, 2, 3, 4, 5, 5, 10, 8, 7 1000]) -> 3
# centered_average([])
# centered_average([1, 2, 3, 4]) => 2

import math

def centered_average(a):
    print(a)
    a.sort()
    print(a)

    middle = a[1:-1]
    print(middle)

    total = 0
    for v in middle:
        total += v

        return total // len(middle)


def centered_average2(a):
    a.remove(max(a))
    a.remove(min(a))

    total = 0
    for v in a:
        total += v
        return total // len(a)


def centered_average3(a):
    mn = min(a)
    mx = max(a)

    total = 0
    for v in a:
        total += v
        
    total -= mn
    total -= mx
    
    return total // len(a)

def centered_average4(a):
    total = 0
    mx = -math.inf
    mn = math.inf

    total = 0
    for v in a:
        total += v
    total -= mn
    total -= mx
    
    return total // len(a)


print(centered_average3([1, 1, 5, 5, 10, 8, 7]))
