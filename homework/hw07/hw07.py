# Probably a die-re situation
import random
random.seed(42)

def dice(a, b):
    """Construct a die that is a list from a to b inclusive.
    >>> dice(1, 6)
    [1, 2, 3, 4, 5, 6]
    >>> dice(3, 5)
    [3, 4, 5]
    >>> dice(5, 5)
    [5]
    """
    return [i for i in range(a,b+1)]

def smallest(die):
    """Return the lowest value die can take on."""
    return min(die)

def largest(die):
    """Return the largest value die can take on."""
    return max(die)

def str_dice(die):
    """Return a string representation of die.

    >>> str_dice(dice(1, 6))
    'die takes on values from 1 to 6'
    """
    return 'die takes on values from {0} to {1}'.format(smallest(die), largest(die))

def roll_dice(die, x):
    """Roll the die x times and return an array of the rolled values.
    >>> roll_dice(dice(5, 5), 4)
    [5, 5, 5, 5]
    >>> max(roll_dice(dice(1, 6), 100))
    6
    >>> min(roll_dice(dice(1, 6), 100))
    1
    >>> x = sum(roll_dice(dice(1, 6), 100))/100 # Finds the mean of 100 dice rolls
    >>> 3 <= x <= 4 # Checks if the mean is between 3 and 4
    True
   """
    a = []
    t = 1
    while(t <= x):
        a = a + [random.choice(die)]
        t= t+ 1
    return a

def rolls_until_six(die):
    """Roll the die until you get a 6 and return the number of rolls it took to do so. 
    If six is not a the possible values to roll, return a string saying '6 is not a possible value of this die'
    >>> rolls_until_six(dice(1, 5))
    '6 is not a possible value of this die'
    >>> rolls_until_six(dice(6, 6)) # Takes one roll to get 6
    1
    >>> x = sum([rolls_until_six(dice(1, 6)) for _ in range(100)])/100 # Repeat 100 times and average
    >>> 5 <= x <= 7 # Check that it takes between 5 and 7 rolls overall on average
    True
    """
    if 6 not in die:
        return '6 is not a possible value of this die'
    else:
        t = 1
        while (random.choice(die) != 6):

            t =t +1
        return t


def cup(die1, die2):
    """Construct a cup that contains die1 and die2.
    >>> cup(dice(1, 1), dice(1, 2))
    [[1], [1, 2]]
    """
    return [die1] + [die2]


def add_to_cup(cup, die):
    """Add die to cup.
    >>> cup1 = cup(dice(1, 1), dice(1, 2))
    >>> add_to_cup(cup1, dice(1, 3))
    [[1], [1, 2], [1, 2, 3]]
    """
    return cup + [die]

def roll_cup(cup):
    """Roll every die in the cup and return an array of the rolled values.
    >>> roll_cup(cup(dice(1, 1), dice(2, 2)))
    [1, 2]
    """
    t = []
    for x in cup:
        t =t+x
    return t
