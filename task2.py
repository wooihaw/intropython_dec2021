# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 16:46:02 2021

@author: wooihaw
"""
# Task 2
alist = ['Python', 'Java', 'Perl', 'PHP', 'JavaScript', 'C++', 'C#', 'Ruby', 'R']

results = [i for i in alist if i[0] == 'P']
print(results)

# Alternative solution using for loop
res2 = []
for i in alist:
    if i[0] == 'P':
        res2.append(i)
print(res2)