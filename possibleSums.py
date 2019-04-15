#!/usr/bin/env python
import sys

#possibleSums #Hash Tables

def possibleSums(coins, quantity):
    """ Main method """
    quantity[0] -= 1
    q = [(coins[0], quantity)]
    sums = set()
    while q:
        val, quans = q.pop()
        sums.add(val)
        if sum(quans) == 0:
            continue
        for i in xrange(len(coins)):
            if quans[i] == 0:
                continue
            q.append((val+coins[i], [0]*(i) + [quans[i]-1] + quans[i:] ))
    return len(sums)

    """
    res = set([])
    for indx in xrange(len(coins)):
        coin = coins[indx]
        quan = quantity[indx]
        print "### Coin %d" % coin
        for q in xrange(quan):
            #print "quan %d" % q
            #add = list()
            add = set()
            for val in res:
                #print "adding: %d" % (val+coin)
                #add.append(val+coin)
                add.add(val+coin)
            if q == 0:
                #print "adding coin %d " % coin
                #add.append(coin)
                add.add(coin)
            res.update(add)
        print "Res = %s" % str(res)
    return len(set(res))"""

def main():
    """ Main flow """
    c = [10, 50, 100] ; q = [1, 2, 1]
    c = [1, 2] ; q = [50000, 2]
    arg = [c, q]
    print "Input:  {0}".format(arg)
    out = possibleSums(c, q)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
