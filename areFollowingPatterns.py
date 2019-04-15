#!/usr/bin/env python
import sys

#areFollowingPatterns #Hash Tables

def areFollowingPatterns(strings, patterns):
    """ Main method """
    mp = dict()
    ms = dict()
    for indx in xrange(len(strings)):
        s = strings[indx]
        p = patterns[indx]
        if mp.get(p) is None:
            mp[p] = s
        if ms.get(s) is None:
            ms[s] = p
        if mp[p] != s or ms[s] != p:
            return False
    return True
    #return len(set(strings)) == len(set(patterns)) == len(set(zip(strings, patterns)))

def main():
    """ Main flow """
    s = ["cat", "dog", "dog"] ; p = ["a", "b", "b"]
    s = ["cat", "dog", "doggy"] ; p = ["a", "b", "b"]
    s = ["cat",  "dog",  "dog"] ; p = ["a", "b", "c"]
    arg = [s, p]
    print "Input:  {0}".format(arg)
    out = areFollowingPatterns(s, p)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
