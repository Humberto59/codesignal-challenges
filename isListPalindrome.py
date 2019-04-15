#!/usr/bin/env python
import sys

#isListPalindrome #Linked List

def isListPalindrome(l):
    """ Main method """
    if l is None or l.next is None:
        return True
    i = 0
    root = l
    while l is not None:
        i += 1 ; l = l.next
    mid = i/2 + i%2
    l = root
    last = None
    for j in xrange(mid):
        nxt = l.next
        l.next = last
        last = l
        l = nxt
    m0 = last
    m1 = l
    if i%2 == 1:
        last = last.next
        mid -= 1
    for j in xrange(mid):
        if l.value != last.value:
            return False
        l = l.next
        last = last.next
    return True


def main():
    """ Main flow """
    arg = []
    print "Input:  {0}".format(arg)
    out = isListPalindrome(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
