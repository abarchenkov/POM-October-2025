# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 11:40:10 2025

@author: abarc
"""

Input = open("input.txt", 'r')
Output = open("output.txt", 'w')
n, m = Input.readline().split(" ")
n, m = int(n), int(m)
Tournament_matches = []
hamiltonian = True
complete = False

for i in range(m):
    rap_battle = Input.readline().strip().split(" ")
    (rap_battle[0], rap_battle[1]) = (int(rap_battle[0]), int(rap_battle[1]))
    Tournament_matches.append(rap_battle)

ordering = Input.readline().split(' ')


counts = [0]*n

for rap_battle in Tournament_matches:
    counts[rap_battle[0] - 1] += 1
    counts[rap_battle[1] - 1] += 1
    

if counts[0] == n - 1 and len(set(counts)) == 1:
    complete = True
    
for i in range(len(ordering)-1):
    if not([int(ordering[i]), int(ordering[i+1])] in Tournament_matches):
        hamiltonian = False
    

if complete:
    Output.write("complete: YES")
else:
    Output.write("complete: NO")
    
if hamiltonian:
    Output.write("\nhamiltonian: YES")
else:
    Output.write("\nhamiltonian: NO")
    
Input.close()
Output.close()