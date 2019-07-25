# Inheritance with cats!

"""
Here's the animal/pet classes!
"""
CURRENT_YEAR = 2019

class Animal(object):
    def __init__(self):
        self.is_alive = True  # It's alive!!

class Pet(Animal):
    def __init__(self, name, year_of_birth, owner=None):
        Animal.__init__(self)   # call the parent's constructor
        self.name = name
        self.age = CURRENT_YEAR - year_of_birth
        self.owner = owner

    def eat(self, thing):
        self.talk()
        if thing == "poison":
            self.lose_life()
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print("..")


#Implement q1 Here!

class Cat(Pet):
    """
    >>> my_cat = Cat("Furball", 2011, "Me", lives=2)
    >>> my_cat.talk()
    Meow!
    >>> my_cat.name
    'Furball'
    >>> my_cat.lose_life()
    >>> my_cat.is_alive
    True
    >>> my_cat.eat("poison")
    Meow!
    Furball ate a poison!
    >>> my_cat.is_alive
    False
    >>> my_cat.lose_life()
    'Cat is dead x_x'
    """
    def __init__(self, name, year_of_birth, owner, lives=9):
        assert type(lives) == int and  lives > 0
        Pet.__init__(self, name, year_of_birth, owner)
        self.lives = lives
        # self.name = name
        # self.year_of_birth = year_of_birth
        # self.owner = owner
        

    def talk(self):
        """A cat says 'Meow!' when asked to talk."""
        print('Meow!')

    def lose_life(self):
        """A cat can only lose a life if it has at least one
        life. When there are zero lives left, the 'is_alive'
        variable becomes False.
        """
        if self.lives > 0:
            self.lives -= 1
            if self.lives == 0:
                self.is_alive = False
        else:
            print("'Cat is dead x_x'")


# T88ble

simple_table_rows = [['chocolate',2], ['vanilla', 1]]
simple_table_labels = ['Flavor', 'Price']
longer_table_rows = [[1990, 1, 1.5, 12, 7], [2000, 2, 2.5, 25, 10], [2010, 5, 4, 70, 36]]
longer_table_labels = ['Year', 'Bread price', 'Eggs price', 'Average tank of gas', 'Rent per day']

class T88ble():
    """
    T88ble is an object similar to the Data 8 Table object.
    Here the internal representation is a list of rows.
    """
    def __init__(self, rows=[], labels=[]):
        self.rows = rows
        self.column_labels = labels
    #DO NOT CHANGE THE __repr__ functions
    def __repr__(self):
        result = ""
        result += str(self.column_labels) + "\n"
        for row in self.rows:
            result += str(row) + "\n"
        return result
    def num_rows(self):
        """
        Compute the number of rows in a table.

        >>> simple_table = T88ble(simple_table_rows, simple_table_labels)
        >>> simple_table.num_rows()
        2
        >>> longer_table = T88ble(longer_table_rows, longer_table_labels)
        >>> longer_table.num_rows()
        3
        """
        return (len(self.rows))
        

    def num_cols(self):
        """
        Compute the number of cols in a table.

        >>> simple_table = T88ble(simple_table_rows, simple_table_labels)
        >>> simple_table.num_cols()
        2
        >>> longer_table = T88ble(longer_table_rows, longer_table_labels)
        >>> longer_table.num_cols()
        5
        """
        return (len(self.rows[0]))
        

    def labels(self):
        """
        Lists the column labels in a table.

        >>> simple_table = T88ble(simple_table_rows, simple_table_labels)
        >>> simple_table.labels()
        ['Flavor', 'Price']
        >>> longer_table = T88ble(longer_table_rows, longer_table_labels)
        >>> longer_table.labels()
        ['Year', 'Bread price', 'Eggs price', 'Average tank of gas', 'Rent per day']
        """
        
        return self.column_labels 
     

    def column(self, label):
        """
        Returns the values of the column represented by label.

        >>> simple_table = T88ble(simple_table_rows, simple_table_labels)
        >>> simple_table.column("Flavor")
        ['chocolate', 'vanilla']
        >>> longer_table = T88ble(longer_table_rows, longer_table_labels)
        >>> longer_table.column("Eggs price")
        [1.5, 2.5, 4]
        >>> longer_table
        ['Year', 'Bread price', 'Eggs price', 'Average tank of gas', 'Rent per day']
        [1990, 1, 1.5, 12, 7]
        [2000, 2, 2.5, 25, 10]
        [2010, 5, 4, 70, 36]
        """
        dis = []
        for x in self.rows:
            dis = dis + [x[self.column_labels.index(label)]]
        return dis
        # return self.rows[self.column_labels.index(label)]

    def with_column(self, label, values):
        """
        Returns a new table with an additional or replaced column.
        label is a string for the name of a column, values is an list

        >>> longer_table = T88ble(longer_table_rows, longer_table_labels)
        >>> longer_table.with_column('Inflation rate', [i for i in range(longer_table.num_rows())])
        ['Year', 'Bread price', 'Eggs price', 'Average tank of gas', 'Rent per day', 'Inflation rate']
        [1990, 1, 1.5, 12, 7, 0]
        [2000, 2, 2.5, 25, 10, 1]
        [2010, 5, 4, 70, 36, 2]
        >>> longer_table
        ['Year', 'Bread price', 'Eggs price', 'Average tank of gas', 'Rent per day']
        [1990, 1, 1.5, 12, 7]
        [2000, 2, 2.5, 25, 10]
        [2010, 5, 4, 70, 36]
        """
        
         
        
        # self.column_labels.append(label)
        # for i in range(len(self.rows)):
        #         self.rows[i].append(values[i]) 
        
        new_label = []
        new_rows = []
        for x in self.column_labels:
            new_label.append(x)
        new_label.append(label)
        
        for i in range(len(self.rows)):
            new_row = []
            new_row += self.rows[i]
        # for i in range(len(b)):    
            new_row.append(values[i])
            new_rows.append(new_row)
            
        
        new_Table = T88ble(new_rows, new_label)

        return new_Table
    def select(self, labels):
        """
        Create a copy of a table with only some of the columns,
        reffered to by the list of labels.

        >>> simple_table = T88ble(simple_table_rows, simple_table_labels)
        >>> simple_table.select(["Flavor"])
        ['Flavor']
        ['chocolate']
        ['vanilla']
        >>> simple_table
        ['Flavor', 'Price']
        ['chocolate', 2]
        ['vanilla', 1]

        >>> longer_table = T88ble(longer_table_rows, longer_table_labels)
        >>> longer_table.select(['Year', 'Average tank of gas'])
        ['Year', 'Average tank of gas']
        [1990, 12]
        [2000, 25]
        [2010, 70]
        >>> longer_table
        ['Year', 'Bread price', 'Eggs price', 'Average tank of gas', 'Rent per day']
        [1990, 1, 1.5, 12, 7]
        [2000, 2, 2.5, 25, 10]
        [2010, 5, 4, 70, 36]
        """
        indexs = []
        
        for i in range(len(labels)):
            indexs.append(self.column_labels.index(labels[i]))
        new_rows = []
        for x in self.rows:
            new_row = []
            for index in indexs:
                new_row.append(x[index])
            new_rows.append(new_row)



        new_Table = T88ble(new_rows, labels)

        return new_Table
        


    def sort(self, label, descending=True):
        """
        Create a copy of a table sorted by the values in a column.
        Defaults to ascending order unless descending = True is included.

        >>> longer_table = T88ble(longer_table_rows, longer_table_labels)
        >>> longer_table.sort("Year")
        ['Year', 'Bread price', 'Eggs price', 'Average tank of gas', 'Rent per day']
        [2010, 5, 4, 70, 36]
        [2000, 2, 2.5, 25, 10]
        [1990, 1, 1.5, 12, 7]
        >>> longer_table
        ['Year', 'Bread price', 'Eggs price', 'Average tank of gas', 'Rent per day']
        [1990, 1, 1.5, 12, 7]
        [2000, 2, 2.5, 25, 10]
        [2010, 5, 4, 70, 36]

        >>> simple_table = T88ble(simple_table_rows, simple_table_labels)
        >>> simple_table.sort("Price", descending=False)
        ['Flavor', 'Price']
        ['vanilla', 1]
        ['chocolate', 2]
        >>> simple_table
        ['Flavor', 'Price']
        ['chocolate', 2]
        ['vanilla', 1]

        """
        new_label = []
        new_rows1 = []
        for x in self.column_labels:
            new_label.append(x)
        
        # self.column_labels.index(label)
        for x in self.rows:
            new_row = []
            new_row += x
            new_rows1.append(new_row)
    
          
        
            
        new_rows = sorted(new_rows1, key=lambda s: s[self.column_labels.index(label)], reverse = descending)
        
        new_Table = T88ble(new_rows, new_label)

        return new_Table
#         students = [['john', 'A', 15], ['jane', 'B', 12], ['dave', 'B', 10]]
# print(sorted(students, key=lambda s: s[2]))  
        


    def where(self, label, filter_fn):
        """
        Create a copy of a table with only the rows that match a filter function.

        >>> def above(x):
        ...     return lambda y: y > x
        ...
        >>> longer_table = T88ble(longer_table_rows, longer_table_labels)
        >>> longer_table.where('Eggs price', above(2))
        ['Year', 'Bread price', 'Eggs price', 'Average tank of gas', 'Rent per day']
        [2000, 2, 2.5, 25, 10]
        [2010, 5, 4, 70, 36]
        >>> longer_table
        ['Year', 'Bread price', 'Eggs price', 'Average tank of gas', 'Rent per day']
        [1990, 1, 1.5, 12, 7]
        [2000, 2, 2.5, 25, 10]
        [2010, 5, 4, 70, 36]
        """
        new_label = []
        new_rows = []
        for x in self.column_labels:
            new_label.append(x)
        # filter(is_even, [1,2,3,4])
        
        for x in self.rows:
            if filter_fn(x[self.column_labels.index(label)]):
                new_row = []
                new_row += x
                new_rows.append(new_row)
        

        new_Table = T88ble(new_rows, new_label)

        return new_Table
