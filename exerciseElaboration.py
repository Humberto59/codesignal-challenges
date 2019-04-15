#!/usr/bin/env python
import sys

#exerciseElaboration #Land of Logic

def exerciseElaboration(p, n):
    """ Main method """
    _num = [str(p)] + ["0"] * n + [str(p)]
    _sqr = int("".join(_num)) ** 2
    return sum( int(x) for x in list(str(_sqr)))

def main():
    """ Main flow """
    p = 5 ; n = 1
    arg = [p, n]
    print "Input:  {0}".format(arg)
    out = exerciseElaboration(p, n)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
"""
p = digit
n = number of zeros between the digits

p = 5
n = 1

(505)^2 = 255025

output = 19
"""
