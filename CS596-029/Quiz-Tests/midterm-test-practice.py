# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 14:42:46 2015

@author: stevenvo
"""

counter = 0
list = [6, 2, 4]
list1 = [1, 3, 5, 7, 9]
def doStuff(list):
    global counter
    for i in list:
        counter += i
    counter /= (len(list)+1)
doStuff(list + list1)
print counter