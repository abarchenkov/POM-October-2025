# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 09:36:00 2025

@author: abarc
"""

Input = open("input.txt", 'r')
Output = open("output.txt", 'w')
n, m = Input.readline().split(" ")
n, m = int(n), int(m)
Tournament_matches = []
ordering = []

for i in range(m):
    rap_battle = Input.readline().strip().split(" ")
    (rap_battle[0], rap_battle[1]) = (int(rap_battle[0]), int(rap_battle[1]))
    Tournament_matches.append(rap_battle)
    
if [1, 2] in Tournament_matches:
    ordering = [1, 2]
else:
    ordering = [2, 1]

for i in range(3, n+1):
    teams_that_i_beat = []
    for j in range(i):
        if[j, i] in Tournament_matches:
            teams_that_i_beat.append(j)
            
    for number in ordering:
        not_done = True
        if not(number in teams_that_i_beat):
            not_done = False
            ordering.insert(ordering.index(number), i)
            break
    if not_done:
        ordering.append(i)
        
order = ''
for number in ordering:
    order += str(number) + ' '
    
Output.write(order)

Input.close()
Output.close()