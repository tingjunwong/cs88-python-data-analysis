######################
# Required Questions #
######################

def arange(start, end, step=1):
    """
    arange behaves just like np.arange(start, end, step).
    You only need to support positive values for step.

    >>> arange(1, 3)
    [1, 2]
    >>> arange(0, 25, 2)
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
    >>> arange(0, 1231, 34)
    [0, 34, 68, 102, 136, 170, 204, 238, 272, 306, 340, 374, 408, 442, 476, 510, 544, 578, 612, 646, 680, 714, 748, 782, 816, 850, 884, 918, 952, 986, 1020, 1054, 1088, 1122, 1156, 1190, 1224]

    """
    cur=list()
    for k in range(start,end,step):
        cur.append(k)
    return cur

    # def n: 
    #     while(n >=0 and r[n] < end):
    #         r[n] = start + step*n
    #     return r[n]
        


def repeated(f, n):
    """Return the function that computes the nth application of f.
    >>> def increment(x):
    ...     return x + 1
    >>> def square(x):
    ...     return x**2
    >>> def triple(x):
    ...     return x*3
    >>> add_three = repeated(increment, 3)
    >>> add_three(5)
    8
    >>> repeated(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> repeated(square, 2)(5) # square(square(5))
    625
    >>> repeated(square, 4)(5) # square(square(square(square(5))))
    152587890625
    """
    def h(x):
        k = 1
        while k <= n:
            x,  k = f(x), k+1
        return x
    return h
    

def compose1(f, g):
    """Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h

def double(f):
    """ Return a function that applies f twice.

    f -- a function that takes one argument

    >>> def square(x):
    ...     return x**2
    >>> double(square)(2)
    16
    """
    def repeated(x):
        return f(f(x))
    return repeated
        

    


def count_cond(condition, n):
    """
    >>> def divisible(n, i):
    ...     return n % i == 0
    >>> count_cond(divisible, 2) # 1, 2
    2
    >>> count_cond(divisible, 4) # 1, 2, 4
    3
    >>> count_cond(divisible, 12) # 1, 2, 3, 4, 6, 12
    6

    >>> def is_prime(n, i):
    ...     return count_cond(divisible, i) == 2
    >>> count_cond(is_prime, 2) # 2
    1
    >>> count_cond(is_prime, 3) # 2, 3
    2
    >>> count_cond(is_prime, 4) # 2, 3
    2
    >>> count_cond(is_prime, 5) # 2, 3, 5
    3
    >>> count_cond(is_prime, 20) # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    def counter(n):
        i, count = 1, 0
        while i <= n:
            if condition(n, i):
                count += 1
            i += 1
        return count
    return counter(n)
    


def match_and_apply(pairs, function):
    """
    >>> pairs = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 0]]
    >>> def square(num):
    ...     return num**2
    >>> func = match_and_apply(pairs, square)
    >>> result = func(3)
    >>> result
    16
    >>> result = func(1)
    >>> result
    4
    >>> result = func(7)
    >>> result
    64
    >>> result = func(15)
    >>> print(result)
    None

    """
    def func(k):
        for pair in pairs:
            if pair[0] == k:
                return function(pair[1])
    return func
    
