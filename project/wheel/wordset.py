from utils import lowercase, key_of_max
import string


#
# WordSet class
#
class WordSet:
    """
    Set of unique words, all in lower case and of positive length.
    """
    def __init__(self, text):
        """
        Form a WordSet from a string of words or collection of words.
        """
        # BEGIN Question 2
        self.text = text
        self.word_set = []
        # END Question 2

    def words(self):
        """
        Return sorted list of words in WordSet.

        >>> WordSet("Hi. Hey you. How, the heck, are you?").words()
        ['are', 'heck', 'hey', 'hi', 'how', 'the', 'you']
        """
        # BEGIN Question 2
        x= str(self.text).lower()
        # m = str(x).translate(string.punctuation)
        y= x.split()

        y = set([''.join(c for c in s if c not in string.punctuation) for s in y])
        y = [s for s in y if s]
        while(len(y) != 0):
            self.word_set.append(min(y))
            y.remove(min(y))


        return self.word_set
        # END Question 2

    def __contains__(self, word):
        # BEGIN Question 2
        if word in self.text:
            return True
        else:
            return False
        # END Question 2


#
# Dictionary class
#
class Dictionary(WordSet):
    """
    Construct a dictionary from all the words in a text file.
    Subclass of WordSet with a file based initializer.

    >>> from wordset import Dictionary
    >>> Dictionary('assets/lincoln.txt').words()[55]
    'government'
    """
    def __init__(self, filename):
        with open(filename) as fp:
            text = fp.read()
            WordSet.__init__(self, text)

#
# WordMunch class
#
class WordMunch(WordSet):
    """
    Perform analytics on a set of unique words.

    Subclass of WordSet that provides analytics on the words.
    """
   
    def filter(self, ffun):
        """Filter set to include only those that satisfy the filter function predicate."""
        # BEGIN
        lst = []
        for item in WordSet(self.text).words():
            # if len(item) == len(ffun):
            #     lst.append(item)
            if ffun(item) == True:
                lst.append(item)
        return lst

        # END

    def frequency(self):
        """Return a dictionary of the frequency of each letter in the word set."""
        # BEGIN
        
        freq = {} 
        # for word in my_list:
        #     for letter in word:
        #         keys=freq.keys()
        #         if letter in keys:
        #             freq[letter]+=1
        #         else:
        #             freq[letter]=1
        # return freq

        whole = ''.join(WordSet(self.text).words())
        
        for m in whole:
            if m in freq:
                freq[m] += 1
            else:
                freq[m] = 1
        return freq
        # END
