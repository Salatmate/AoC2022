import sys
import aoc
test = '''Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi'''
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
def part1(inp):
    grid = defaultdict(lambda:100)
    for y in range(len(inp)):
        for x in range(len(inp[0])):
            if inp[y][x] == 'S':
                start = (x,y)
                grid[(x,y)] = 0
            elif inp[y][x] == 'E':
                end = (x,y)
                grid[(x,y)] = 25
            else: grid[(x,y)] = ord(inp[y][x]) - ord('a')
    paths = [(0,start)]
    visited = set()
    while paths:
        steps,path = paths.pop(0)
        if path in visited: continue
        if path == end:
            print(steps)
            break
        visited.add(path)
        for adj in aoc.adj4(path):
            if adj not in visited and grid[adj] <= grid[path]+1:
                paths.append((steps+1,adj))

def part2(inp):
    grid = defaultdict(lambda:100)
    for y in range(len(inp)):
        for x in range(len(inp[0])):
            if inp[y][x] == 'S': grid[(x,y)] = 0
            elif inp[y][x] == 'E':
                end = (x,y)
                grid[(x,y)] = 25
            else: grid[(x,y)] = ord(inp[y][x]) - ord('a')
    ans = 1000000
    for y in range(len(inp)):
        start = (0,y)
        paths = [(0,start)]
        visited = set()
        while paths:
            steps,path = paths.pop(0)
            if path in visited: continue
            if path == end:
                ans = min(ans,steps)
                break
            visited.add(path)
            for adj in aoc.adj4(path):
                if adj not in visited and grid[adj] <= grid[path]+1:
                    paths.append((steps+1,adj))
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