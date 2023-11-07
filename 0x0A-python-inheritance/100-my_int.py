#!/usr/bin/python3
"""MyInt class"""


class MyInt(int):
    """
    MyInt class is a rebel

    Reverse the expected output
    """
    def __eq__(self, number):
        """
        equal method
        """
        return super().__ne__(number)

    def __ne__(self, number):
        """
        not equal method
        """
        return super().__eq__(number)
