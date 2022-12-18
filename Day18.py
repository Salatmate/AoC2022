import sys
import aoc
test = '''2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5'''
file = open(sys.argv[0].split('\\')[-1].replace('py','txt'),'r')
raw_inp = file.read()
file.close()

def parseInput(inp):
    inp = aoc.cleanInput(inp,',-:')
    inp = inp.split('\n') #split into lines
    #inp = [int(i) for i in inp] #convert each line into integer
    inp = [[int(j) for j in i.split()] for i in inp]
    #inp = [i.split(' ') for i in inp] #convert each line into list
    #inp = [[int(j) for j in i.split(' ')] for i in inp] #convert each line into list
    return inp

inp = parseInput(raw_inp)
try: test = parseInput(test)
except Exception: pass

from collections import defaultdict
def part1(inp):
    grid = defaultdict(lambda:False)
    for i in inp: grid[tuple(i)] = True
    ans = 0
    for x,y,z in inp:
        if not grid[(x-1,y,z)]: ans += 1
        if not grid[(x+1,y,z)]: ans += 1
        if not grid[(x,y-1,z)]: ans += 1
        if not grid[(x,y+1,z)]: ans += 1
        if not grid[(x,y,z-1)]: ans += 1
        if not grid[(x,y,z+1)]: ans += 1
    print(ans)
def adj6(pos):
    x,y,z = pos
    return [(x,y-1,z),(x-1,y,z),(x,y+1,z),(x+1,y,z),(x,y,z+1),(x,y,z-1)]
def part2(inp):
    grid = defaultdict(lambda:False)
    for i in inp: grid[tuple(i)] = True
    ans = 0
    lx = (min(grid,key=lambda x:x[0]))[0]-1
    ux = (max(grid,key=lambda x:x[0]))[0]+1
    ly = (min(grid,key=lambda x:x[1]))[1]-1
    uy = (max(grid,key=lambda x:x[1]))[1]+1
    lz = (min(grid,key=lambda x:x[2]))[2]-1
    uz = (max(grid,key=lambda x:x[2]))[2]+1
    steam = [(lx,ly,lz)]
    visited = set()
    while steam:
        curr = steam.pop(-1)
        if curr in visited: continue
        visited.add(curr)
        
        for x,y,z in adj6(curr):
            if (x,y,z) not in visited and lx <= x <= ux and ly<=y<=uy and lz<=z<=uz and not grid[(x,y,z)]:
                steam.append((x,y,z))
            if grid[(x,y,z)]:
                ans += 1
    print(ans)
    
print('Part 1:')
part1(inp)
try:
    print('Part 1 Test:')
    part1(test)
except Exception: pass
print('Part 2:')
part2(inp)
try:
    print('Part 2 Test:')
    part2(test)
except Exception: pass