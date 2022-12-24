import sys
import aoc
test = '''#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#'''
file = open(sys.argv[0].split('\\')[-1].replace('py','txt'),'r')
raw_inp = file.read()
file.close()

def parseInput(inp):
    inp = aoc.cleanInput(inp,',-:')
    inp = inp.split('\n') #split into lines
    #inp = [int(i) for i in inp] #convert each line into integer
    #inp = [[int(j) for j in i.split('\n')] for i in inp]
    #inp = [i.split(' ') for i in inp] #convert each line into list
    #inp = [[int(j) for j in i.split(' ')] for i in inp] #convert each line into list
    return inp

inp = parseInput(raw_inp)
try: test = parseInput(test)
except Exception: pass

from collections import defaultdict
from copy import copy
from math import lcm
start=0;end=0;grid=defaultdict(lambda:False);adj=[0,-1,0,1,0,0];time=0;lc=0
def part1(inp):
    global start,end,grid,adj,time,lc
    blizzards = set()
    for y in range(len(inp)):
        for x in range(len(inp[0])):
            if inp[y][x] == '.': 
                if y == 0: start = (x,y)
                if y+1 == len(inp): end = (x,y)
            if inp[y][x] == '^': blizzards.add((x,y,0))
            if inp[y][x] == '<': blizzards.add((x,y,1))
            if inp[y][x] == 'v': blizzards.add((x,y,2))
            if inp[y][x] == '>': blizzards.add((x,y,3))
            if inp[y][x] == '#': blizzards.add((x,y,4))
            if inp[y][x] != '.': grid[(0,x,y)] = True
    wx,wy = end[0]+1,end[1]
    lc = lcm(wx-1,wy-1)
    grid[(0,start[0],-1)] = True
    grid[(0,end[0],end[1]+1)] = True
    for time in range(1,lc):
        new = set()
        grid[(time,start[0],-1)] = True
        grid[(time,end[0],end[1]+1)] = True
        for x,y,f in blizzards:
            if (0 < x+adj[f] < wx and 0 < y+adj[f+1] < wy) or f==4:
                new.add((x+adj[f],y+adj[f+1],f))
                grid[(time,x+adj[f],y+adj[f+1])] = True
            elif x+adj[f] == 0:
                new.add((wx+adj[f],y,f))
                grid[(time,wx+adj[f],y)] = True
            elif x+adj[f] == wx:
                new.add((adj[f],y,f))
                grid[(time,adj[f],y)] = True
            elif y+adj[f+1] == 0:
                new.add((x,wy+adj[f+1],f))
                grid[(time,x,wy+adj[f+1])] = True
            elif y+adj[f+1] == wy:
                new.add((x,adj[f+1],f))
                grid[(time,x,adj[f+1])] = True
        blizzards = copy(new)
    paths = [(0,start)]
    time = -1
    visited = set()
    while paths:
        time,pos = paths.pop(0)
        if ((time+1)%lc,pos) in visited:
            continue
        visited.add(((time+1)%lc,pos))
        if pos == end:
            print(time)
            break
        x,y = pos
        for i in range(5):
            if not grid[((time+1)%lc,x+adj[i],y+adj[i+1])] and ((time+1)%lc,x+adj[i],y+adj[i+1]) not in visited:
                paths.append((time+1,(x+adj[i],y+adj[i+1])))

def part2(inp):
    global start,end,grid,adj,time,lc
    paths = [(time,end)]
    visited = set()
    while paths:
        time,pos = paths.pop(0)
        if ((time+1)%lc,pos) in visited:
            continue
        visited.add(((time+1)%lc,pos))
        if pos == start:
            print(time)
            break
        x,y = pos
        for i in range(5):
            if not grid[((time+1)%lc,x+adj[i],y+adj[i+1])] and ((time+1)%lc,x+adj[i],y+adj[i+1]) not in visited:
                paths.append((time+1,(x+adj[i],y+adj[i+1])))
    paths = [(time,start)]
    visited = set()
    while paths:
        time,pos = paths.pop(0)
        if ((time+1)%lc,pos) in visited:
            continue
        visited.add(((time+1)%lc,pos))
        if pos == end:
            print(time)
            break
        x,y = pos
        for i in range(5):
            if not grid[((time+1)%lc,x+adj[i],y+adj[i+1])] and ((time+1)%lc,x+adj[i],y+adj[i+1]) not in visited:
                paths.append((time+1,(x+adj[i],y+adj[i+1])))
    
print('Part 1:')
part1(inp)
print('Part 2:')
part2(inp)