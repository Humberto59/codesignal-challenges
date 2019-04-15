#!/usr/bin/env python
import sys

#rotateImage 

def rotateImage(a):
    """ Main method """
    return zip(*a[::-1])

def main():
    """ Main flow """
    arg = []
    print "Input:  {0}".format(arg)
    out = rotateImage(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
