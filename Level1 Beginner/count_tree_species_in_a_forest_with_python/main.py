"""
https://dailypythonprojects.substack.com/p/count-tree-species-in-a-forest-with

Project Description

Your task for today is simple. You should make a program that takes a list of tree species found in a forest and counts how many times each species appears.

trees = ["oak", "pine", "maple", "oak", "birch", "pine", "oak"]
"""

trees = ["oak", "pine", "maple", "oak", "birch", "pine", "oak"]

forest = {}
for tree in trees:
    if tree in forest:
        forest[tree]+=1
    else:
        forest[tree]=1


for tree in forest:
    print(f"{tree}: {forest[tree]}")