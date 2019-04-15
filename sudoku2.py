#!/usr/bin/env python
import sys
from collections import Counter
#sudoku2 

def sudoku2(grid):
    """ Main method """
    for indx in xrange(9):
        row = grid[indx]
        col = zip(*grid)[indx]
        if is_valid(row) is False or is_valid(col) is False:
            return False
    for i in xrange(0, 9, 3):
        for j in xrange(0, 9, 3):
            tmp = grid[i][j:j+3] + grid[i+1][j:j+3] + grid[i+2][j:j+3]
            if is_valid(tmp) is False:
                return False
    return True

def is_valid(vals=None):
    count = Counter(vals)
    if count.get(".") is not None:
        del count["."]
    return True if sum(count.values()) == len(count.values()) else False

def main():
    """ Main flow """
    arg = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
           ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
           ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
           ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
           ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
           ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
           ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
           ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
           ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
    arg = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
           ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
           ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
           ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
           ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
           ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
           ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
           ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
           ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
    print "Input:  {0}".format(arg)
    out = sudoku2(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
