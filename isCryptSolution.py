#!/usr/bin/env python
import sys

#isCryptSolution 

def isCryptSolution(crypt, solution):
    """ Main method """
    sol = dict()
    for x, y in solution:
        sol[x] = int(y)
    if not is_valid(crypt[0], sol) or \
        not is_valid(crypt[1], sol) or \
        not is_valid(crypt[2], sol):
        return False
    if translate(crypt[0], sol) + \
        translate(crypt[1], sol) != \
        translate(crypt[2], sol):
        return False
    return True

def is_valid(word, sol):
    if sol[word[0]] == 0 and len(word) != 1:
        return False
    return True

def translate(word, sol):
    res = 0
    for c in word:
        res = res * 10 + sol[c]
    return res

def main():
    """ Main flow """
    crypt = ["SEND", "MORE", "MONEY"]
    solution = [['O', '0'],
            ['M', '1'],
            ['Y', '2'],
            ['E', '5'],
            ['N', '6'],
            ['D', '7'],
            ['R', '8'],
            ['S', '9']]
    crypt = ["TEN", "TWO", "ONE"]
    solution = [['O', '1'],
            ['T', '0'],
            ['W', '9'],
            ['E', '5'],
            ['N', '4']]

    arg = [crypt, solution]
    print "Input:  {0}".format(arg)
    out = isCryptSolution(crypt, solution)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
"""
https://app.codesignal.com/interview-practice/task/yM4uWYeQTHzYewW9H
"""
