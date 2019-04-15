#!/usr/bin/env python
import sys

#hasPathWithGivenSum #Trees

def hasPathWithGivenSum(t, s):
    """ Main method """
    return traversal(t, 0, s)

def traversal(node, total, s):
    if node is None:
        return False
    total += node.value
    if node.left is not None:
        if traversal(node.left, total, s) is True:
            return True
    if node.right is not None:
        return traversal(node.right, total, s)
    return total == s and node.left is None and node.right is None

def main():
    """ Main flow """
    arg = []
    print "Input:  {0}".format(arg)
    out = hasPathWithGivenSum(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
