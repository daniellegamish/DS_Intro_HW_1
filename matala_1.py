# -*- coding: utf-8 -*-
"""
matala 1

Danielle Gamish
205454127
"""

## A:
    
def  my_func(x1, x2, x3):
    if isinstance(x1, float) or isinstance(x2, float) or isinstance(x3, float):
        return ('Error: parameters should be float')
    
    if (x1 + x2 + x3) == 0 :
        return ('Not a number – denominator equals zero')
    
    else: 
        return (((x1 + x2 + x3) * (x2 + x3) * x3) / (x1 + x2 + x3))

## B:
# Set the value to zero per minute for cases where the user enters only one value such as: 1.75 which is an one hour and 45 minutes    
def convert(hours, minutes=0):
    if hours < 0 or minutes < 0 :
        return ('Input error!')
    
    else:
        return ((hours*60*60)+(minutes*60))
    
