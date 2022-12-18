import sys
import aoc
test = '''>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'''
file = open(sys.argv[0].split('\\')[-1].replace('py','txt'),'r')
raw_inp = file.read()
file.close()

def parseInput(inp):
    inp = aoc.cleanInput(inp,',-:')
    #inp = [int(i) for i in inp] #convert each line into integer
    #inp = [[int(j) for j in i.split('\n')] for i in inp]
    #inp = [i.split(' ') for i in inp] #convert each line into list
    #inp = [[int(j) for j in i.split(' ')] for i in inp] #convert each line into list
    return inp

inp = parseInput(raw_inp)
try: test = parseInput(test)
except Exception: pass

blocks = '''####

.#.
###
.#.

..#
..#
### 

#
#
#
#

##
##'''.split('\n\n')
blocks = [i.split('\n') for i in blocks]
from collections import defaultdict
def part1(inp):
    global blocks
    grid = defaultdict(lambda:False)
    high = 0
    jet = 0
    for block in range(2022):
        curr = (blocks[block%5])
        x,y = (3,high-3-len(curr))
        while True:
            if inp[jet] == '>':
                shift = 1
            else: shift = -1
            flag = True
            for dy in range(len(curr)):
                for dx in range(len(curr[dy])):
                    if curr[dy][dx] == '#' and not (not grid[(x+dx+shift,y+dy)] and 1 <= x+dx+shift <= 7):
                        flag = False
                        break
                if not flag: break
            if flag:
                x += shift
                
            flag = True
            for dy in range(len(curr)):
                for dx in range(len(curr[dy])):
                    if curr[dy][dx] == '#' and not (not grid[(x+dx,y+dy+1)] and -1 >= y+dy+1):
                        flag = False
                        break
                if not flag: break
            if flag:
                y += 1
            else:
                for dy in range(len(curr)):
                    for dx in range(len(curr[dy])):
                        if curr[dy][dx] == '#': grid[(x+dx,y+dy)] = True
                        
                high = min(high,y)
                jet += 1
                jet %= len(inp)
                break
            
            jet += 1
            jet %= len(inp)
    print(abs(high))

def part2(inp):
    global blocks
    grid = defaultdict(lambda:False)
    high = 0
    jet = 0
    trillion = int(1e12)
    heights = defaultdict(lambda:0)
    for block in range(50455*1000):
        curr = (blocks[block%5])
        x,y = (3,high-3-len(curr))
        while True:
            if inp[jet] == '>':
                shift = 1
            else: shift = -1
            flag = True
            for dy in range(len(curr)):
                for dx in range(len(curr[dy])):
                    if curr[dy][dx] == '#' and not (not grid[(x+dx+shift,y+dy)] and 1 <= x+dx+shift <= 7):
                        flag = False
                        break
                if not flag: break
            if flag:
                x += shift
                
            flag = True
            for dy in range(len(curr)):
                for dx in range(len(curr[dy])):
                    if curr[dy][dx] == '#' and not (not grid[(x+dx,y+dy+1)] and -1 >= y+dy+1):
                        flag = False
                        break
                if not flag: break
            if flag:
                y += 1
            else:
                for dy in range(len(curr)):
                    for dx in range(len(curr[dy])):
                        if curr[dy][dx] == '#': grid[(x+dx,y+dy)] = True
                high = min(high,y)
                jet += 1
                jet %= len(inp)
                break
            
            jet += 1
            jet %= len(inp)
        if heights[(block%5,jet)]: 
            start,starth = heights[(block%5,jet)]
            cycle = block - start
            iters = (trillion-start)//cycle
            hdiff = starth - high
            end = trillion - iters*cycle - start
            endh = heights[[i for i in heights if heights[i][0] == start+end][0]][1]
            if end == 0:
                print(iters*hdiff-endh-1)
                break
        heights[(block%5,jet)] = (block,high)
    
print('Part 1:')
part1(inp)
print('Part 1 Test:')
part1(test)
print('Part 2:')
part2(inp)
try:
    print('Part 2 Test:')
    part2(test)
except Exception: pass