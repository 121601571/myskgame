import sys,os

class card:

    def __init__(self, name, fun, idx=0, ):
        self.name =name
        self.fun = fun
        self.idx = idx

    def __str__(self):
        return self.name+'_'+self.fun

    