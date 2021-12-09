# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 16:50:48 2021

@author: wooihaw
"""
# Task 3
import statistics as stat

temperatures = []
with open('Heathrow.txt', 'r') as f:
    for line in f:
        temperatures.append(float(f.readline().strip()))

print(temperatures)

print(f'Minimum: {min(temperatures)}')
print(f'Maximum: {max(temperatures)}')
print(f'Mean: {stat.mean(temperatures)}')
print(f'Median: {stat.median(temperatures)}')