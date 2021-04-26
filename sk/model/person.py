import sys,os
import card
class person:

    def __init__(self, name, skilllist, maxhp):
        self.maxhp = maxhp
        self.curhp = maxhp
        self.name = name
        self.skillist = skilllist

    def __str__(self):
        return self.name


    