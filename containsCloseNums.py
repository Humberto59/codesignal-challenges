#!/usr/bin/env python
import sys

#containsCloseNums #Hash Tables

def containsCloseNums(nums, k):
    """ Main method """
    _map = dict()
    for indx in xrange(len(nums)):
        num = nums[indx]
        if _map.get(num) is None:
            _map[num] = indx
            continue
        if indx - _map[num] <= k:
            return True
        _map[num] = indx
    return False

def main():
    """ Main flow """
    n = [0, 1, 2, 3, 5, 2] ; k =3
    arg = [n, k]
    print "Input:  {0}".format(arg)
    out = containsCloseNums(n, k)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
