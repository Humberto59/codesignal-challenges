#!/usr/bin/env python
import sys

#rearrangeLastN #Linked List

def rearrangeLastN(l, n):
    """ Main method """
    if n == 0:
        return l
    # cut, root, list
    c = r = l
    for _ in xrange(n):
        if l is None:
            return l
        l = l.next
    while l.next is not None:
        c, l = c.next, l.next
    cn = c.next
    c.next = None
    l.next = r
    return cn

def main():
    """ Main flow """
    arg = []
    print "Input:  {0}".format(arg)
    out = rearrangeLastN(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
