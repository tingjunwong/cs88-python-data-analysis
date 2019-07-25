## Debug This
def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2  * 0
    0
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return n * skip_mul(n - 2)


## MapReduce

def map(f, s):
    """
    Map a function f onto a sequence.

    >>> def double(x):
    ...     return x * 2
    >>> def square(x):
    ...     return x ** 2
    >>> def toLetter(x):
    ...     alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ...     return alpha[x%26]
    >>> map(double, [1,2,3,4])
    [2, 4, 6, 8]
    >>> map(square, [1, 2, 3, 4, 5, 10])
    [1, 4, 9, 16, 25, 100]
    >>> map(toLetter, [3, 0, 19, 0])
    ['d', 'a', 't', 'a']

    """
    if s == []:
        return s
    return [f(s[0])] + map(f, s[1:])


def filter(f, s):
    """Filter a sequence to only contain values allowed by filter.

    >>> def is_even(x):
    ...     return x % 2 == 0
    >>> def divisible_by5(x):
    ...     return x % 5 == 0
    >>> filter(is_even, [1,2,3,4])
    [2, 4]
    >>> filter(divisible_by5, [1, 4, 9, 16, 25, 100])
    [25, 100]
    """
    return[num for num in s if f(num)]
    


from operator import add, mul

def reduce(reducer, s, base):
    """Reduce a sequence under a two-argument function starting from a base value.

    >>> def add(x, y):
    ...     return x + y
    >>> def mul(x, y):
    ...     return x*y
    >>> reduce(add, [1,2,3,4], 0)
    10
    >>> reduce(mul, [1,2,3,4], 0)
    0
    >>> reduce(mul, [1,2,3,4], 1)
    24
    """
    result = base
    for num in s:
        result = reducer(result, num)
    return result
    


# Recursive Math

def count_digit(n, digit):
    """Return how many times digit appears in n.

    >>> count_digit(55055, 5)
    4
    >>> count_digit(1231421, 1)
    3
    >>> count_digit(12, 3)
    0
    """
    if n ==0:
        return 0
    if n % 10 == digit :
        return count_digit(n//10,digit) + 1
    else:
        return count_digit(n//10,digit)

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    def helper(n):
        if n < 10:
            return 0
        else:
            return count_digit(n // 10,10 - n % 10) + helper(n // 10)

    return helper(n)



# Challenge

def decimal(n):
    """Return a list representing the decimal representation of a number.

    >>> decimal(55055)
    [5, 5, 0, 5, 5]
    >>> decimal(-136)
    ['-', 1, 3, 6]
    """
    if (n>0):
        if (n<10):
            return [n]
        else:
            return decimal(n//10)+ [n%10]
    else:
        n=n*(-1)
        if (n<10):
            return [n]
        else:
            return ['-']+decimal(n//10)+ [n%10]


def binary(n):
    """Return a list representing the representation of a number in base 2.

    >>> binary(55055)
    [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]
    >>> binary(-136)
    ['-', 1, 0, 0, 0, 1, 0, 0, 0]
    """
    if (n>0):
        if (n<2):
            return [n]
        else:
            return binary(n//2)+ [n%2]
    else:
        n=n*(-1)
        if (n<2):
            return [n]
        else:
            return ['-']+binary(n//2)+ [n%2]

