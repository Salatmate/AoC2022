import sys
import aoc
test = '''....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..'''
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
    grid = defaultdict(lambda:False)
    elves = []
    for y in range(len(inp)):
        for x in range(len(inp[y])):
            if inp[y][x] == '#':
                grid[(x,y)] = True
                elves.append((x,y))
    for time in range(10):
        consider = defaultdict(lambda:0)
        moveto = defaultdict(lambda:0)
        for x,y in elves:
            if not any([grid[i] for i in aoc.adj8((x,y))]):
                moveto[(x,y)] = (x,y)
            elif not any([grid[(x,y-1)],grid[(x-1,y-1)],grid[(x+1,y-1)]]) and time%4<=0:
                moveto[(x,y)] = (x,y-1)
                consider[(x,y-1)] += 1
            elif not any([grid[(x,y+1)],grid[(x-1,y+1)],grid[(x+1,y+1)]]) and time%4<=1:
                moveto[(x,y)] = (x,y+1)
                consider[(x,y+1)] += 1
            elif not any([grid[(x-1,y)],grid[(x-1,y-1)],grid[(x-1,y+1)]]) and time%4<=2:
                moveto[(x,y)] = (x-1,y)
                consider[(x-1,y)] += 1
            elif not any([grid[(x+1,y)],grid[(x+1,y-1)],grid[(x+1,y+1)]]):
                moveto[(x,y)] = (x+1,y)
                consider[(x+1,y)] += 1
            elif not any([grid[(x,y-1)],grid[(x-1,y-1)],grid[(x+1,y-1)]]) and time%4>=1:
                moveto[(x,y)] = (x,y-1)
                consider[(x,y-1)] += 1
            elif not any([grid[(x,y+1)],grid[(x-1,y+1)],grid[(x+1,y+1)]]) and time%4>=2:
                moveto[(x,y)] = (x,y+1)
                consider[(x,y+1)] += 1
            elif not any([grid[(x-1,y)],grid[(x-1,y-1)],grid[(x-1,y+1)]]) and time%4>=3:
                moveto[(x,y)] = (x-1,y)
                consider[(x-1,y)] += 1
            else:
                moveto[(x,y)] = (x,y)
        grid = defaultdict(lambda:False)
        for i in range(len(elves)):
            if consider[moveto[elves[i]]] == 1:
                elves[i] = moveto[elves[i]]
            grid[elves[i]] = True
    xw = abs(min(elves)[0]-max(elves)[0])+1
    yw = abs(min(elves,key=lambda x:x[1])[1]-max(elves,key=lambda x:x[1])[1])+1
    print(xw*yw-len(elves))
            

def part2(inp):
    grid = defaultdict(lambda:False)
    elves = []
    for y in range(len(inp)):
        for x in range(len(inp[y])):
            if inp[y][x] == '#':
                grid[(x,y)] = True
                elves.append((x,y))
    for time in range(100000):
        consider = defaultdict(lambda:0)
        moveto = defaultdict(lambda:0)
        notmove = 0
        for x,y in elves:
            if not any([grid[i] for i in aoc.adj8((x,y))]):
                moveto[(x,y)] = (x,y)
                notmove += 1
            elif not any([grid[(x,y-1)],grid[(x-1,y-1)],grid[(x+1,y-1)]]) and time%4<=0:
                moveto[(x,y)] = (x,y-1)
                consider[(x,y-1)] += 1
            elif not any([grid[(x,y+1)],grid[(x-1,y+1)],grid[(x+1,y+1)]]) and time%4<=1:
                moveto[(x,y)] = (x,y+1)
                consider[(x,y+1)] += 1
            elif not any([grid[(x-1,y)],grid[(x-1,y-1)],grid[(x-1,y+1)]]) and time%4<=2:
                moveto[(x,y)] = (x-1,y)
                consider[(x-1,y)] += 1
            elif not any([grid[(x+1,y)],grid[(x+1,y-1)],grid[(x+1,y+1)]]):
                moveto[(x,y)] = (x+1,y)
                consider[(x+1,y)] += 1
            elif not any([grid[(x,y-1)],grid[(x-1,y-1)],grid[(x+1,y-1)]]) and time%4>=1:
                moveto[(x,y)] = (x,y-1)
                consider[(x,y-1)] += 1
            elif not any([grid[(x,y+1)],grid[(x-1,y+1)],grid[(x+1,y+1)]]) and time%4>=2:
                moveto[(x,y)] = (x,y+1)
                consider[(x,y+1)] += 1
            elif not any([grid[(x-1,y)],grid[(x-1,y-1)],grid[(x-1,y+1)]]) and time%4>=3:
                moveto[(x,y)] = (x-1,y)
                consider[(x-1,y)] += 1
            else:
                moveto[(x,y)] = (x,y)
                notmove += 1
        grid = defaultdict(lambda:False)
        for i in range(len(elves)):
            if consider[moveto[elves[i]]] == 1:
                elves[i] = moveto[elves[i]]
            elif moveto[elves[i]] != elves[i]: notmove += 1
            grid[elves[i]] = True
        if notmove==len(elves):
            aoc.visual(grid)
            print(time+1)
            break
        if time % 100 == 0: print(time,notmove,len(elves))
    
print('Part 1:')
part1(inp)
print('Part 1 Test:')
part1(test)
print('Part 2:')
part2(inp)
try:
    print('Part 2 Test:')
    #part2(test)
except Exception: pass