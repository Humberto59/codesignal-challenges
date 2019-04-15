#!/usr/bin/env python
import sys
from Common import build_linked_list, print_linked_list

#reverseNodesInKGroups #Linked List

def reverseNodesInKGroups(l, k):
    """ Main method """
    if k == 1:
        return l
    # root
    r = ListNode(None)
    r.next = l
    # previous
    p = r
    # prev source, source -> target = list
    ps = s = None
    i = 0
    while l is not None:
        i += 1
        if i % k == 1:
            ps = p
            s = l
        ln = l.next
        if i % k == 0:
            _p = None
            _l = s
            for _i in xrange(k):
                _nxt = _l.next
                _l.next = _p
                _p = _l
                _l = _nxt

            ps.next = l
            s.next = ln

            p = s
            l = ln
            continue
        p = l
        l = ln
    return r.next

def main():
    """ Main flow """
    #l = [1, 2, 3, 4, 5] ; k = 2
    #l = [1, 2, 3, 4, 5] ; k = 1
    #l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] ; k = 3
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] ; k = 4
    #l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] ; k = 4
    arg = [l, k]
    print "Input:  {0}".format(arg)
    out = reverseNodesInKGroups(build_linked_list(l), k)
    print "output: "
    print_linked_list(out)


class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


if __name__ == '__main__':
    sys.exit(main())
