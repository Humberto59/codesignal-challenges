#!/usr/bin/env python
import sys

#removeKFromList #Linked List

def removeKFromList(l, k):
    """ Main method """
    root = l
    last = None
    while True:
        if l is None:
            break
        if l.value == k:
            if l == root:
                root = l.next
                l = root
                continue
            l = l.next
            last.next = l
            continue
        last = l
        l = l.next
    return root

def main():
    """ Main flow """
    arg = []
    print "Input:  {0}".format(arg)
    out = removeKFromList(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
