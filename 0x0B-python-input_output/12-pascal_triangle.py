#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """
    Pascal's trianglr list of lists
    Args:
        n (int): number
    Return:
        a list of lists
    """
    if n <= 0:
        return []

    lists = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(lists[i-1][j-1] + lists[i-1][j])
        row.append(1)
        lists.append(row)

    return lists
