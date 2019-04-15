#!/usr/bin/env python
import sys

#firstDuplicate #Land of Logic

def firstDuplicate(a):
    """ Main method """
    _map = dict()
    for i in a:
        if _map.get(i) is None:
            _map[i] = True
            continue
        return i
    return -1

def main():
    """ Main flow """
    arg = []
    print "Input:  {0}".format(arg)
    out = firstDuplicate(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
