"""Lab 2: Functions """

## Coding
def a_or_c(grade):
    """
    We all know the saying "C's get degrees".
    We all would like to get an A, but sometimes
    a C will have to do. 

    Return whether the grade inputted
    would receive an A or C.

    >>> a_or_c(100)
    True
    >>> a_or_c(75)
    True
    >>> a_or_c(82)
    False
    >>> a_or_c(80)
    False
    >>> a_or_c(95)
    True
    >>> a_or_c(40)
    False
    """
    return(90<=grade<=100) or (70<= grade <=79)

def min(x, y):
    """
    Return the minimum between x and y

    >>> min(1,2)
    1
    >>> min(3,1)
    1
    >>> min(2,3)
    2
    >>> min(0, 67777)
    0
    >>> min(-1, -5)
    -5
    >>> min(-7, -1)
    -7
    >>> min(0, 0)
    0
    """
    if (x < y):
        return x
    else:
        return y



def abs_value_equal(x, y):
    """Return whether or not the absolute value of both numbers is the same.

    Please refrain from using libraries (abs)

    >>> abs_value_equal(-2, -2)
    True
    >>> abs_value_equal(-3, 3)
    True
    >>> abs_value_equal(1, 2)
    False
    >>> abs_value_equal(3, 3)
    True
    >>> abs_value_equal(-6, -6)
    True
    >>> abs_value_equal(-1, -5)
    False
    >>> abs_value_equal(5, -6)
    False
    """
    return ((x==y) or (x+y==0)) 


   


## Representation

def mirror(num1, num2):
    """
    Return if num1 is num2 backwards
    The inputs will always be < 100.

    >>> mirror(12, 21)
    True
    >>> mirror(54, 45)
    True
    >>> mirror(33, 33)
    True
    >>> mirror(42, 52)
    False
    >>> mirror(12, 22)
    False
    """
    return ((num1//10==num2%10) and (num2//10==num1%10))
    

