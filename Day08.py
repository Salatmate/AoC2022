import sys
test = '''30373
25512
65332
33549
35390'''
file = open(sys.argv[0].split('\\')[-1].replace('py','txt'),'r')
raw_inp = file.read()
file.close()

def adj4(pos):
    x,y = pos
    return [(x,y-1),(x-1,y),(x,y+1),(x+1,y)]
def adj8(pos):
    x,y = pos
    return [(x,y-1),(x-1,y-1),(x-1,y),(x-1,y+1),(x,y+1),(x+1,y+1),(x+1,y),(x+1,y-1)]
def visual(grid,flipX=False,flipY=False):
    output = ''
    positions = list(grid.keys())
    if not flipY:
        for y in range(min(positions,key=lambda x:x[1])[1],max(positions,key=lambda x:x[1])[1]):
            if not flipX:
                for x in range(min(positions,key=lambda x:x[0])[0],max(positions,key=lambda x:x[0])[0]):
                    output += grid[(x,y)]
            else:
                for x in reversed(range(min(positions,key=lambda x:x[0])[0],max(positions,key=lambda x:x[0])[0])):
                    output += grid[(x,y)]
            output += '\n'
    else:
        for y in reversed(range(min(positions,key=lambda x:x[1])[1],max(positions,key=lambda x:x[1])[1])):
            if not flipX:
                for x in range(min(positions,key=lambda x:x[0])[0],max(positions,key=lambda x:x[0])[0]):
                    output += grid[(x,y)]
            else:
                for x in reversed(range(min(positions,key=lambda x:x[0])[0],max(positions,key=lambda x:x[0])[0])):
                    output += grid[(x,y)]
            output += '\n'
    print(output)

def cleanInput(inp,filter):
    for char in filter:
        inp = inp.replace(char,' ')
    return inp
def parseInput(inp):
    inp = cleanInput(inp,',-:')
    inp = inp.split('\n') #split into lines
    #inp = [int(i) for i in inp] #convert each line into integer
    inp = [[int(j) for j in list(i)] for i in inp]
    #inp = [i.split(' ') for i in inp] #convert each line into list
    #inp = [[int(j) for j in i.split(' ')] for i in inp] #convert each line into list
    return inp

inp = parseInput(raw_inp)
try: test = parseInput(test)
except Exception: pass

from collections import defaultdict
def part1(inp):
    ans = 0
    vis = defaultdict(lambda:False)
    grid = defaultdict(lambda:0)
    for y in range(len(inp)):
        for x in range(len(inp[0])):
            grid[(x,y)] = inp[y][x]
    for y in range(len(inp)):
        highest = -1
        for x in range(len(inp[0])):
            if grid[(x,y)] > highest and not vis[(x,y)]:
                ans += 1
                vis[(x,y)] = True
            if grid[(x,y)] > highest:
                highest = grid[(x,y)]
        highest = -1
        for x in reversed(range(len(inp[0]))):
            if grid[(x,y)] > highest and not vis[(x,y)]:
                ans += 1
                vis[(x,y)] = True
            if grid[(x,y)] > highest:
                highest = grid[(x,y)]
    for x in range(len(inp)):
        highest = -1
        for y in range(len(inp[0])):
            if grid[(x,y)] > highest and not vis[(x,y)]:
                ans += 1
                vis[(x,y)] = True
            if grid[(x,y)] > highest:
                highest = grid[(x,y)]
        highest = -1
        for y in reversed(range(len(inp[0]))):
            if grid[(x,y)] > highest and not vis[(x,y)]:
                ans += 1
                vis[(x,y)] = True
            if grid[(x,y)] > highest:
                highest = grid[(x,y)]
    print(ans)

def part2(inp):
    ans = 0
    vis = defaultdict(lambda:False)
    grid = defaultdict(lambda:99)
    for y in range(len(inp)):
        for x in range(len(inp[0])):
            grid[(x,y)] = inp[y][x]
    for y in range(len(inp)):
        for x in range(len(inp[0])):
            curr = 1
            if x == 0 or x == len(inp)-1 or y == 0 or y == len(inp)-1: continue
            for d in range(1,y+1):
                if grid[(x,y-d)] >= grid[(x,y)]:
                    curr *= d
                    break
            else: curr *= d
            for d in range(1,len(inp)-y):
                if grid[(x,y+d)] >= grid[(x,y)]:
                    curr *= d
                    break
            else: curr *= d
            for d in range(1,x+1):
                if grid[(x-d,y)] >= grid[(x,y)]:
                    curr *= d
                    break
            else: curr *= d
            for d in range(1,len(inp)-x):
                if grid[(x+d,y)] >= grid[(x,y)]:
                    curr *= d
                    break
            else: curr *= d
            ans = max(ans,curr)
                
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