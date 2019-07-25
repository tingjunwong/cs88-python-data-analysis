from secret import SecretWord
from board import Board

class Game:
    """Run an entire game.

    Initialization defines the player who pickers secret word and one or more guessers.
    play
       - picker picks the secret word from the dictionary held by all players
       - guessers guess in turn looking at the state of the board until the game is done
       - each guesser continues as long as they guess correct letters
       - returns final board
    winner returns the player who picked the last letter.
    """
    def __init__(self, picker, guessers):
        # BEGIN
        self.picker = picker
        self.guessers = guessers
        self.a = picker.pick_word()
        self.b = Board(SecretWord(self.a))
        # END

    def play(self, verbose=True):
        # BEGIN
        
        # i = 0      
        # while(i < len(self.guessers)):
        # if (verbose == False):
        #     return
        # while (not self.b.done()):
        # for i in range(len(self.guessers)):
        i = 0
        while ( i <= len(self.guessers)):
            # while self.guessers[i].guess(self.b) in self.a:
            #     self.guessers[i].guess(self.b)

            while self.b.guess(self.guessers[i].guess(self.b)) > 0:
                if self.b.done():
                    return self.b
                else:
                    # self.b.guess(self.guessers[i].guess(self.b))
                    continue

            # while self.b.guess(input()) > 0:
            #     self.b.guess(input())
            # while self.b.guess(self.guessers[i].guess(self.b)) == 0:
            else:
                if i < len(self.guessers) - 1:
                    i = i + 1
                    continue
                elif i == len(self.guessers) - 1:
                    continue


        return self.b

        # END

    def winner(self):
        # BEGIN
        self.play(True)
        return guessers[i]
        # END
