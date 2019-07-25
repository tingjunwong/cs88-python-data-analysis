"""Player classes for Wheel of Fortune game."""

from wordset import WordMunch
from wordset import Dictionary
from utils import *
import random
# from random import sample

class Player:
    """Player base class.  Defines initializer and interface.

    >>> from wordset import Dictionary
    >>> p = Player("Fred", Dictionary('assets/lincoln.txt'))
    >>> p.possible_words[2]
    'add'
    """
    def __init__(self, name, dictionary=Dictionary('assets/lincoln.txt')):
        """Inialize the class with a dictionary of words the player can guess from."""
        # BEGIN
        self.name= name
        # self.dictionary = Dictionary('assets/lincoln.txt')
        self.possible_words = dictionary.words()
        # END

    def guess(self, board):
        """Guesses a character and returns it."""
        return None

    def pick_word(self):
        """Return a word that is to be guessed."""
        return None

class DummyPlayer(Player):
    """Simple deterministic player for testing."""

    def __init__(self, name):
        self.name = name
        self.calls = -1

    def guess(self, board):
        """Return the guesses [c,f,e,o,r,s]."""
        self.calls += 1
        return "cfeors"[self.calls]

    def pick_word(self):
        """Sets the dummy word as `score` and returns it."""
        return 'score'


class HumanPlayer(Player):
    """
    HumanPlayer is initialized with a name and implements the player interface
    such that:
    - guess requests a guess from a person, via the input device
    - pick_word requests a secret word and verifies that it is in the dictionary
    """
    def __init__(self, dict=Dictionary('assets/lincoln.txt'), name='Human'):
        """Creates a player with the name and word set"""
        super().__init__(name, dict)

    def guess(self, board):
        """Asks the user to guess a character."""

        print(self.name, ", please enter your next guess.")
        guess = input()
        while (len(guess) != 1) or (guess in board.guesses()):
            print('Please enter a single character not yet guessed')
            guess = input()
        return guess

    def pick_word(self):
        """
        Requests a word from user to use as a secret words.
        Only allows words from the dictionary.
        """
        print(self.name,", pick your secret word.")
        word = input()
        while not word in self.possible_words:
            print(word, " is not in the dictionary. Another:")
            word = input()
        return word

class ComputerPlayer(Player):
    """
    Perform as a player - picking a word or guessing a character
    See the unlock test for examples
    """
    def __init__(self, dict=Dictionary('assets/lincoln.txt'), skill=0, name='Computer'):
        """Creates a player with the name, dict, and skill level"""
        # # Replace this when you get to question 5
        super().__init__(name,dict)
        # BEGIN
        # self.name = name
        self.skill = skill
        # self.dict = dict
        # self.text = text
        # END

    def guess(self, board):
        """
        Guess a character to play based on the current board
        Uses different strategies based on the players skill level
        Break ties alphabetically, key_of_max does this automatically:)
        """
        # BEGIN
        # lst= []
        if self.skill == 0:
            b = WordMunch(self.possible_words).frequency()
            a =  key_of_max(b)
            while a in board.guesses():
                b.pop(a)
                a = key_of_max(b)

            return a
            
            
        elif self.skill == 1:
            def compare(item):
                if len(item) == len(board.secret.word):
                    return True

            b = WordMunch(WordMunch(self.possible_words).filter(compare)).frequency()
            a =  key_of_max(b)
            while a in board.guesses():
                b.pop(a)
                a = key_of_max(b)

            return a

        elif self.skill == 2:
            def compare1(item):
                if len(item) ==len(board.secret.word):
                    return True
            c = WordMunch(self.possible_words).filter(compare1)
            e = WordMunch(c).frequency()


            def compare2(item):

                i = 0
                m = board.guesses()[len(board.guesses()) - 1]

                for n in board.secret.match(m):

                    if item[n] != m:
                        # i = i + 1
                        return False
                    else:
                        i = i + 1
                        if i == len(board.secret.match(m)):
                            return True 
            
            
            a =  key_of_max(e)
            while a in board.guesses():
                d = WordMunch(c).filter(compare2)
                b = WordMunch(d).frequency()
                b.pop(a)

                a = key_of_max(b)

            return a


    def pick_word(self):
        """Pick a random word from the dictionary."""
        from random import sample
        return "".join(random.sample(Dictionary('assets/lincoln.txt').words(), 1))
        # END


