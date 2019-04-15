#!/usr/bin/env python
import sys

#groupingDishes #Hash Tables

def groupingDishes(dishes):
    """ Main method """
    _map = dict()
    for dish in dishes:
        dsh = dish.pop(0)
        for ingr in dish:
            if _map.get(ingr) is None:
                _map[ingr] = list([dsh])
                continue
            _map[ingr].append(dsh)
    res = list()
    for ingr in sorted(_map.keys()):
        if len(_map[ingr]) == 1:
            continue
        res.append([ingr] + sorted(_map[ingr]))
    return res

def main():
    """ Main flow """
    arg = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
           ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
           ["Quesadilla", "Chicken", "Cheese", "Sauce"],
           ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]
    print "Input:  {0}".format(arg)
    out = groupingDishes(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
