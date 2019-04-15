#!/usr/bin/env python
import sys

#mergeTwoLinkedLists #Linked List

def mergeTwoLinkedLists(l1, l2):
    """ Main method """
    r = l3 = ListNode(None)
    while l1 is not None or l2 is not None:
        if l1 and l2:
            if l1.value < l2.value:
                l3.next = ListNode(l1.value)
                l1 = l1.next
            else:
                l3.next = ListNode(l2.value)
                l2 = l2.next
            l3 = l3.next
            continue
        if l1 is None:
            l3.next  = ListNode(l2.value)
            l2 = l2.next
        else:
            l3.next = ListNode(l1.value)
            l1 = l1.next
        l3 = l3.next

    return r.next

def main():
    """ Main flow """
    arg = []
    print "Input:  {0}".format(arg)
    out = mergeTwoLinkedLists(arg)
    print "output: {0}".format(out)


class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

if __name__ == '__main__':
    sys.exit(main())
