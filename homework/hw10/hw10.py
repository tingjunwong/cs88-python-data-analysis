 ################
#### Person ####
################

class Person(object):
    """Person class.

    >>> steven = Person("Steven")
    >>> steven.say("Hello")
    'Hello'
    >>> steven.repeat()
    'Hello'
    >>> steven.greet()
    'Hello, my name is Steven'
    >>> steven.repeat()
    'Hello, my name is Steven'
    >>> steven.ask("preserve abstraction barriers")
    'Would you please preserve abstraction barriers'
    >>> steven.repeat()
    'Would you please preserve abstraction barriers'
    """
    def __init__(self, name):
        self.name = name
        self.newstuff = None

    def say(self, stuff):
        self.newstuff = stuff
        return stuff

    def ask(self, stuff):
        return self.say("Would you please " + stuff)

    def greet(self):
        return self.say("Hello, my name is " + self.name)

    def repeat(self):
        return self.newstuff


##############
#### Errors ####  
##############


class Error:
    """
    >>> err1 = Error(12, "error.py")
    >>> err1.write()
    'error.py:12'

    """
    def __init__(self, line, file):
        self.line = line
        self.file = file

    def write(self):
        return self.file + ':' + str(self.line)

class SyntaxError(Error):
    """
    >>> err1 = SyntaxError(17, "HW10.py")
    >>> err1.write()
    HW10.py:17 SyntaxError : Invalid syntax
    >>> err1.add_code(4, "EOL while scanning string literal")
    >>> err2 = SyntaxError(18, "HW10.py", 4)
    >>> err2.write()
    HW10.py:18 SyntaxError : EOL while scanning string literal

    """
    type = 'SyntaxError'
    msgs = {0 : "Invalid syntax", 1: "Unmatched parentheses", 2: "Incorrect indentation", 3: "missing colon"}

    def __init__(self, line, file, code=0):
        self.line = line
        self.file = file
        self.code = code
    def write(self):
        end = self.type + ' : ' + self.msgs.get(self.code)
        print(self.file + ':' + str(self.line) + " " + end)

    def add_code(self, code, msg):
        self.msgs[code] = msg


class ZeroDivisionError(Error):
    """
    >>> err1 = ZeroDivisionError(273, "HW10.py")
    >>> err1.write()
    HW10.py:273 ZeroDivisionError : division by zero
    """
    type = 'ZeroDivisionError'

    def __init__(self, line, file, message='division by zero'):
        self.line = line
        self.file = file
        self.message = message
    def write(self):
        end = self.type + ' : ' + self.message
        print(self.file + ':' + str(self.line) + " " + end)

