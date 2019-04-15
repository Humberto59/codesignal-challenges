#!/usr/bin/env python
import sys

#firstNotRepeatingCharacter 

def firstNotRepeatingCharacter(s):
    """ Main method """
    _map = dict()
    for i in xrange(len(s)):
        c = s[i]
        if _map.get(c) is None:
            _map[c] = [i, 1]
            continue
        _map[c][1] += 1

    for k in _map.keys():
        if _map[k][1] > 1:
            del _map[k]
            continue
        _map[k] = _map[k][0]
    print "map = " + str(_map)

    return min(_map.items(), key=lambda x : x[1])[0] if _map else "_"

def main():
    """ Main flow """
    #arg = "abacacad"
    arg = 'abacabaabacaba'
    print "Input:  {0}".format(arg)
    out = firstNotRepeatingCharacter(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
