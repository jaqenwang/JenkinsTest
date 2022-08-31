import sys
import os
import itertools as it

class Comb:
    def __init__(self,str,m):
        self.str = str
        self.m = m

    def calc(self):
        l1 = it.permutations(self.str,self.m)
        count = 0
        for e in l1:
            print(''.join(e))
            count += 1
        return count

if __name__ == '__main__':
    combtest = Comb('123',3)
    combtest.calc()
