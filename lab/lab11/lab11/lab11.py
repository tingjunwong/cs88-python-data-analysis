#############
# Iterators #
#############

# Q2
class IteratorRestart:
    """
    >>> iterator = IteratorRestart(2, 7)
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    """
    def __init__(self, start, end):
        self.start = 2
        self.end = 7
        self.a = 2
    def __next__(self):
        if self.start > self.end:
            self.start = self.a
            raise StopIteration
        self.start += 1
        return self.start - 1

    def __iter__(self):
        return self


# Q3
class Str:
    """
    >>> s = Str("hello")
    >>> for c in s:
    ...     print(c)
    ...
    h
    e
    l
    l
    o
    
    >>> for c in s:
    ...     print(c)
    """
    def __init__(self, word):
        self.word = word
        self.e = 0
    def __next__(self):
        
        if self.e >= len(self.word):
            raise StopIteration
        self.e += 1
        return self.word[self.e - 1]
        
        
        
    def __iter__(self):
        return self




##############
# Generators #
##############

# Q4
def countdown(n):
    """
    >>> from types import GeneratorType
    >>> type(countdown(0)) is GeneratorType # countdown is a generator
    True
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    
    while n >= 0:
        yield n
        n -= 1

class Countdown:
    """
    >>> from types import GeneratorType
    >>> type(Countdown(0)) is GeneratorType # Countdown is an iterator
    False
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    def __init__(self, n):
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.n < 0:
            raise StopIteration
        self.n -= 1
        return self.n + 1

# Q5
def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
  
    while n >= 1:
        
        if n % 2 == 0:
            yield n
            n = n//2
            
        else:
            yield n
            if n == 1:
                return
            if n > 1:
                n = 3 * n + 1
    

