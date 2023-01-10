#!/usr/bin/python3

class MyList(list):
    """
    MyList is a class that inherits from the built-in list class in Python,
    and also has a method `print_sorted` that prints the list in ascending order
    """
    def __init__(self):
        """
        initialize the object, call the parent's class __init__
        """
        super().__init__()
        
    def print_sorted(self):
        """
        This method prints the sorted version of the MyList
        It does not change the original unsorted list
        """
        print(sorted(self))

