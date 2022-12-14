import sys
import aoc
test = '''498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9'''
file = open(sys.argv[0].split('\\')[-1].replace('py','txt'),'r')
raw_inp = file.read()
file.close()

def parseInput(inp):
    inp = aoc.cleanInput(inp,'->')
    inp = inp.split('\n') #split into lines
    #inp = [int(i) for i in inp] #convert each line into integer
    #inp = [[int(j) for j in i.split('\n')] for i in inp]
    #inp = [i.split(' ') for i in inp] #convert each line into list
    #inp = [[int(j) for j in i.split(' ')] for i in inp] #convert each line into list
    return inp

inp = parseInput(raw_inp)
try: test = parseInput(test)
except Exception: pass

def manhattan(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

from collections import defaultdict
def part1(inp):
    grid = defaultdict(lambda:0)
    lowy = 0
    for i in inp:
        i = [[int(j) for j in j.split(',')] for j in i.split()]
        for j in range(len(i)-1):
            minx = min(i[j][0],i[j+1][0])
            miny = min(i[j][1],i[j+1][1])
            maxx = max(i[j][0],i[j+1][0])
            maxy = max(i[j][1],i[j+1][1])
            lowy = max(lowy,maxy)
            if minx==maxx:
                for dy in range(0,maxy-miny+1):
                    grid[(minx,miny+dy)] = 1
            else:
                for dx in range(0,maxx-minx+1):
                    grid[(minx+dx,miny)] = 1
    sand = 0
    pos = [500,0]
    while pos[1] < lowy:
        pos = [500,0]
        while pos[1] < lowy:
            x,y = pos
            if not grid[(x,y+1)]:
                pos = (x,y+1)
            elif not grid[(x-1,y+1)]:
                pos = (x-1,y+1)
            elif not grid[(x+1,y+1)]:
                pos = (x+1,y+1)
            else:
                grid[(x,y)] = 2
                break
        sand += 1
    for y in range(0,lowy+3):
        out = ''
        for x in range(450,551):
            if grid[(x,y)] == 1: out += '█'
            elif grid[(x,y)] == 2: out += '░'
            else: out += '.'
        print(out)
    print(sand-1)
        

def part2(inp):
    grid = defaultdict(lambda:0)
    lowy = 0
    for i in inp:
        i = [[int(j) for j in j.split(',')] for j in i.split()]
        for j in range(len(i)-1):
            minx = min(i[j][0],i[j+1][0])
            miny = min(i[j][1],i[j+1][1])
            maxx = max(i[j][0],i[j+1][0])
            maxy = max(i[j][1],i[j+1][1])
            lowy = max(lowy,maxy)
            if minx==maxx:
                for dy in range(0,maxy-miny+1):
                    grid[(minx,miny+dy)] = 1
            else:
                for dx in range(0,maxx-minx+1):
                    grid[(minx+dx,miny)] = 1
    sand = 0
    for x in range(1000):
        grid[(x,lowy+2)] = True
    while not grid[(500,0)]:
        pos = [500,0]
        while True:
            x,y = pos
            if not grid[(x,y+1)]:
                pos = (x,y+1)
            elif not grid[(x-1,y+1)]:
                pos = (x-1,y+1)
            elif not grid[(x+1,y+1)]:
                pos = (x+1,y+1)
            else:
                grid[(x,y)] = 2
                break
        sand += 1
    for y in range(0,lowy+3):
        out = ''
        for x in range(450,551):
            if grid[(x,y)] == 1: out += '█'
            elif grid[(x,y)] == 2: out += '░'
            else: out += '.'
        print(out)
    print(sand)
    
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