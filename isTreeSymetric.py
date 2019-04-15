#!/usr/bin/env python
import sys

#isTreeSymetric #Hash Tables

def isTreeSymetric(t):
    """ Main method """
    if t is None:
        return True
    li = [t.left, t.right]
    while sum(map(lambda x : 0 if x is None else x.value, li)):
        n_li = list()
        vals = list()
        for node in li:
            if node is None:
                vals.append(None)
                n_li += [None, None]
                continue
            vals.append(node.value)
            n_li.append(node.left)
            n_li.append(node.right)
        for indx in xrange(len(vals)/2):
            if vals[indx] != vals[-(1+indx)]:
                return False
        li = n_li

    return True

def main():
    """ Main flow """
    arg = []
    print "Input:  {0}".format(arg)
    out = isTreeSymetric(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
