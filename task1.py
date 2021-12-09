# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 16:41:04 2021

@author: wooihaw
"""
# Task 1
heads = 35
legs = 94

for r in range(36):
    c = heads - r
    if 2*c + 4*r == legs:
        print(f'There are {c} chickens and {r} rabbits')