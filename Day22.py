import sys
import aoc
test = '''        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5'''
file = open(sys.argv[0].split('\\')[-1].replace('py','txt'),'r')
raw_inp = file.read()
file.close()

def parseInput(inp):
    inp = aoc.cleanInput(inp,',-:')
    inp = inp.replace('R',' R ')
    inp = inp.replace('L',' L ')
    inp = inp.split('\n\n') #split into lines
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
    instr = inp[1].split()
    adj = [0,-1,0,1,0]
    grid = defaultdict(lambda:0)
    tiles = inp[0].split('\n')
    pos = False
    for y in range(len(tiles)):
        for x in range(len(tiles[y])):
            if tiles[y][x] == '.': grid[(x+1,y+1)] = 1
            if tiles[y][x] == '#': grid[(x+1,y+1)] = 2
            if tiles[y][x] == '.' and not pos: pos = (x+1,y+1)
    f = 3
    for inst in instr:
        try:
            inst = int(inst)
            x,y = pos
            for step in range(inst):
                if grid[(x+adj[f],y+adj[f+1])] == 1:
                    x += adj[f]
                    y += adj[f+1]
                elif grid[(x+adj[f],y+adj[f+1])] == 2:
                    break
                else:
                    cx,cy = pos
                    while grid[(cx,cy)] != 0:
                        cx -= adj[f]
                        cy -= adj[f+1]
                    if grid[(cx+adj[f],cy+adj[f+1])] == 1:
                        x = cx+adj[f]
                        y = cy+adj[f+1]
                    elif grid[(cx+adj[f],cy+adj[f+1])] == 2:
                        break
            #print(pos,(x,y),f)
            pos = (x,y)
        except ValueError:
            if inst == 'R': f = (f-1)%4
            if inst == 'L': f = (f+1)%4
    print(pos[1]*1000+pos[0]*4+3-f)

def part2(inp):
    instr = inp[1].split()
    adj = [0,-1,0,1,0]
    grid = defaultdict(lambda:0)
    tiles = inp[0].split('\n')
    pos = False
    for y in range(len(tiles)):
        for x in range(len(tiles[y])):
            if tiles[y][x] == '.': grid[(x,y)] = 1
            if tiles[y][x] == '#': grid[(x,y)] = 2
            if tiles[y][x] == '.' and not pos: pos = (x,y)
    #print(pos)
    f = 3
    for inst in instr:
        try:
            inst = int(inst)
            x,y = pos
            for step in range(inst):
                #print(x,y,f)
                if grid[(x+adj[f],y+adj[f+1])] == 1:
                    x += adj[f]
                    y += adj[f+1]
                elif grid[(x+adj[f],y+adj[f+1])] == 2:
                    break
                else:
                    cx,cy = x%50,y%50
                    gx,gy = x//50,y//50
                    if (gx,gy,f) == (1,0,0):
                        cf = 3
                        cx,cy = (50*0,50*3+cx)
                    elif (gx,gy,f) == (0,3,1):
                        cf = 2
                        cx,cy = (50*1+cy,50*0)
                        
                    elif (gx,gy,f) == (1,0,1):
                        cf = 3
                        cx,cy = (50*0,50*2+49-cy)
                    elif (gx,gy,f) == (0,2,1):
                        cf = 3
                        cx,cy = (50*1,50*0+49-cy)
                        
                    elif (gx,gy,f) == (1,1,1):
                        cf = 2
                        cx,cy = (50*0+cy,50*2)
                    elif (gx,gy,f) == (0,2,0):
                        cf = 3
                        cx,cy = (50*1,50*1+cx)
                        
                    elif (gx,gy,f) == (1,2,2):
                        cf = 1
                        cx,cy = (50*0+49,50*3+cx)
                    elif (gx,gy,f) == (0,3,3):
                        cf = 0
                        cx,cy = (50*1+cy,50*2+49)
                        
                    elif (gx,gy,f) == (1,2,3):
                        cf = 1
                        cx,cy = (50*2+49,50*0+49-cy)
                    elif (gx,gy,f) == (2,0,3):
                        cf = 1
                        cx,cy = (50*1+49,50*2+49-cy)
                        
                    elif (gx,gy,f) == (1,1,3):
                        cf = 0
                        cx,cy = (50*2+cy,50*0+49)
                    elif (gx,gy,f) == (2,0,2):
                        cf = 1
                        cx,cy = (50*1+49,50*1+cx)
                        
                    elif (gx,gy,f) == (2,0,0):
                        cf = 0
                        cx,cy = (50*0+cx,50*3+49)
                    elif (gx,gy,f) == (0,3,2):
                        cf = 2
                        cx,cy = (50*2+cx,50*0)
                    else:
                        print((x,y),(gx,gy,f),(cx,cy))
                        input()
                    #input(((x,y,f),(cx,cy,cf)))
                    if grid[(cx,cy)] == 1:
                        x,y,f = cx,cy,cf
                    elif grid[(cx,cy)] == 2:
                        break
                    
            pos = (x,y)
        except ValueError:
            if inst == 'R': f = (f-1)%4
            if inst == 'L': f = (f+1)%4
    print((pos[1]+1)*1000+(pos[0]+1)*4+3-f)
    
print('Part 1:')
part1(inp[:])
print('Part 1 Test:')
part1(test)
print('Part 2:')
part2(inp[:])
print('Part 2 Test:')
#part2(test)