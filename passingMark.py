#!/usr/bin/env python
import sys

#passingMark #Land of Logic

def passingMark(passMark, grades):
    """ Main method """
    g = map(lambda x : float(abs(ord(x)-70)), grades)
    p = sum(g) / float(len(g))
    return p >= passMark

def main():
    """ Main flow """
    p = 3.5 ; g = "ABC"
    arg = [p, g]
    print "Input:  {0}".format(arg)
    out = passingMark(p, g)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
