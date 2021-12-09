# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 16:56:40 2021

@author: wooihaw
"""
# Task 4
from collections import Counter

with open('alice.txt', 'r') as f:
    s = f.read()

t = [c.lower() if c.isalpha() else ' ' for c in s]
w = ''.join(t)
allwords = w.split()
print(allwords)

word_freq = Counter(allwords)
print(f'Most common 10 words: {word_freq.most_common(10)}')
print(f'The word "alice" occurs {word_freq["alice"]} times')