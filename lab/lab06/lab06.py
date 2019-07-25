
"""Lab 6: Review """

## Coding

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    
    if k % 10 == 7:
        return True
    else:
        if k<10:
            return False
        return has_seven(k//10)


def deep_len(lst):
    """Returns the deep length of the list.

    >>> deep_len([1, 2, 3])     # normal list
    3
    >>> x = [1, [2, 3], 4]      # deep list
    >>> deep_len(x)
    4
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> deep_len(x)
    6
    """
    s=0
    for x in lst:
        if type(x) == list:
            s = s + deep_len(x)


        else:
            s=s+1
    return s


def polynomial(degree, coeffs):
    """
    >>> fourth = polynomial(4, [3,6,2,1, 100])
    >>> fourth(3)   # 3*(3**4) + 6*(3**3) + 2*(3**2) + 1*(3**1) + 100
    526
    >>> third = polynomial(3, [2, 0, 0, 0])
    >>> third(4)   # 2*(4**3) + 0*(4**2) + 0*(4**1) + 0
    128
    """

    def h(x):
        result = 0
        degre=degree
        for i in range(len(coeffs)):
            result = result + coeffs[i]*(x**degre)
            degre = degre - 1
        return result
        

        def h(x):
        result = 0
        nonlocal degree
        for i in range(len(coeffs)):
            result = result + coeffs[i]*(x**degree)
            degree = degree - 1
        return result





    return h

    # def h(x):
    #     result = 0
    #     for i in range(degree, -1, -1):
    #         result = result + coeffs[degree - i]*(x**i)
            
    #     return result
    


    # return h



def add_matrices(x, y):
    """
    >>> matrix1 = [[1, 3],
    ...            [2, 0]]
    >>> matrix2 = [[-3, 0],
    ...            [1, 2]]
    >>> add_matrices(matrix1, matrix2)
    [[-2, 3], [3, 2]]
    """
    return [[x[i][j] + y[i][j]  for j in range(len(x[0]))] for i in range(len(x))]
        


    


def mul_by_num(num):
    """
    Returns a function that takes one argument and returns num
    times that argument.
    >>> x = mul_by_num(5)
    >>> y = mul_by_num(2)
    >>> x(3)
    15
    >>> y(-4)
    -8
    """
    def h(x):
        return num * x


    return h
    


def skip_add(n):
    """ Takes a number x and returns x + x-2 + x-4 + x-6 + ... + 0.

    >>> skip_add(5)  # 5 + 3 + 1 + 0
    9
    >>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
    30
    """
    



    if n ==0:
        return 0
    if n ==1:
        return 1
    else:
        return n + skip_add(n-2)




