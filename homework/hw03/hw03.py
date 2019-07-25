######################
# Required Questions #
######################

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 10)  # 4 * 3 * 2 * 1 # Only n times!!
    24
    """
    if (n > k):
        total, stop = 1, n-k
        while n > stop:
            total, n = total*n, n-1
        
    else:
        total = 1
        while (n >1):
            total, n=total*n, n-1

    return total

def nonzero(lst):
    """ Returns the first nonzero element of a list

    >>> nonzero([1, 2, 3])
    1
    >>> nonzero([0, 1, 2])
    1
    >>> nonzero([0, 0, 0, 0, 0, 0, 5, 0, 6])
    5
    """
    for x in lst:
        if (x != 0):
            return x



def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    length = 1
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n // 2      # Integer division prevents "1.0" output
        else:
            n = 3 * n + 1
        length = length + 1
    print(n)                # n is now 1
    return length


def odd_even(x):
    """Classify a number as odd or even.
    
    >>> odd_even(4)
    'even'
    >>> odd_even(3)
    'odd'
    """
    if x % 2==0:
        return 'even'
    else:
        return 'odd'

def classify(s):
    """
    Classify all the elements of a sequence as odd or even
    >>> classify([0, 1, 2, 4])
    ['even', 'odd', 'even', 'even']
    """
    
    return [odd_even(x)for x in s]


def decode_helper(pair):
    """
    Optional helper function! Could be useful to turn something like [0, 0] to 'Male 0-9'
    """
    a=''
    if pair[0] ==0:
        a= a+'Male'
    else:
        a= a+'Female'
    y=pair[1]
    if y==0:
        a=a + ' 0-9'
    if y==1:
        a=a + ' 10-19'
    if y==2:
        a=a +  ' 20-29'
    if y==3:
        a=a +  ' 30-39'
    if y==4:
        a=a + ' 40-49'
    if y==5:
        a=a +  ' 50-59'
    if y==6:
        a=a +  ' 60-69'
    if y==7:
        a=a + ' 70-79'
    if y==8:
        a=a +  ' 80-89'
    if y==9:
        a=a + ' 90-99'
    if y==10:
        a=a +  ' 100+'
    return a

    
    

def decode(list_of_sex_age_pairs):
    """
    >>> decode([[0, 0], [1, 1], [1, 10]])
    ['Male 0-9', 'Female 10-19', 'Female 100+']
    >>> decode([[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]])
    ['Male 0-9', 'Male 10-19', 'Male 20-29', 'Male 30-39', 'Male 40-49', 'Female 50-59', 'Female 60-69', 'Female 70-79', 'Female 80-89', 'Female 90-99', 'Female 100+']
    """ 
    a=[]
    for x in list_of_sex_age_pairs:
        a.append(decode_helper(x))
    return a

