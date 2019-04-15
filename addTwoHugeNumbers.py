#!/usr/bin/env python
import sys
from Common import build_linked_list, print_linked_list

#addTwoHugeNumbers #Linked List

def addTwoHugeNumbers(a, b):
    """ Main method """
    c = read_num(a) + read_num(b)
    if c == 0:
        return ListNode(0)
    r = li = ListNode(None)
    while c > 0:
        num = c % 10000
        c /= 10000
        li.next = ListNode(num)
        li = li.next
    li = r = r.next
    last = None
    while li is not None:
        nxt = li.next
        li.next = last
        last = li
        li = nxt
    return last

def read_num(li):
    num = 0
    while li is not None:
        num *= 10000
        num += li.value
        li = li.next
    return num

def main():
    """ Main flow """
    a = [123, 4, 5] ; b = [100, 100, 100]
    arg = [a, b]
    print "Input:  {0}".format(arg)
    out = addTwoHugeNumbers(build_linked_list(a), build_linked_list(b))
    print "output: "
    print_linked_list(out)


class ListNode(object):
   def __init__(self, x):
     self.value = x
     self.next = None

if __name__ == '__main__':
    sys.exit(main())
