"""Board class for Wheel of Fortune game."""

class Board:
    """Board for Wheel of Fortune with attributes board and guessed.
    Attributes:
       board - list of correct characters or "_" in the secret word
       guessed - list of characters guessed so far

    >>> from secret import SecretWord
    >>> b = Board(SecretWord("bookkeeper"))
    >>> len(b)
    10
    >>> b.guess('o')
    2
    >>> b
    < _ o o _ _ _ _ _ _ _ : o >
    >>> b.done()
    False
    >>> b.guess('k')
    2
    >>> b
    < _ o o k k _ _ _ _ _ : o,k >
    >>> b.guess('j')
    0
    >>> b
    < _ o o k k _ _ _ _ _ : o,k,j >
    >>> b.word()
    ['_', 'o', 'o', 'k', 'k', '_', '_', '_', '_', '_']
    >>> b.guesses()
    ['o', 'k', 'j']
    """
    def __init__(self, secret):
        """Create an initial board with no guesses and a secret."""
        # BEGIN
        self.secret = secret
        self.new = []
        # END

    def __repr__(self):
        return '< ' + " ".join(self.word()) + " : " + ",".join(self.guesses()) + ' >'

    def __len__(self):
        return self.word_len()

    def word_len(self):
        """Return the length of the secret word."""
        # BEGIN
        return len(self.secret.word)
        # END

    def word(self):
        """Return the current state of guessing the word as a list of characters.
        Unguessed positions are represented by '_'
        Guessed positions hold the character.
        """
        # BEGIN
        a = list(self.secret.word)
        b = self.hits()
        # for m in a:
        #     if m not in self.hits():
        #         m = '_'
        # return a
        rep = ['_' if x not in b else x for x in a]
        return rep


        # END

    def guesses(self):
        """Return a list of the characters guessed so far."""
        # BEGIN
        return self.new
        # END

    def hits(self):
        """Return a list of characters correctly guessed."""
        # BEGIN
        z = []
        for m in self.secret.word:
            if m in self.guesses():
                z.append(m)
        return z
        # END

    def misses(self):
        """Return a list of characters incorrectly guessed."""
        # BEGIN
        y = []
        for m in self.guesses():
            if m not in self.secret.word:
                y.append(m)
        return y
        # END

    def guess(self, char):
        """Update the board to reflect the guess of char.
        Return the number of indices in the secret word where char occurs.
        If char does not appear in the word, this will be 0.
        """
        # BEGIN
        # if char in self.secret.word:

        # else:
        #     return 0
        self.new.append(char)
        return list(self.secret.word).count(char)
        # END

    def done(self):
        """Determine if the game is done."""
        # BEGIN
        if '_' in self.word():
            return False
        else:
            return True
        # END

    def display(self):
        print(self.word())
        print("Guessed chars: ", self.guesses())
