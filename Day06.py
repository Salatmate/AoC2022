import sys
test = '''bvwbjplbgvbhsrlpgdmjqwftvncz'''
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
    inp = cleanInput(inp,',-')
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
    for i in range(3,len(inp)):
        if len(set(inp[i-3:i+1])) == 4:
            print(i+1)
            break

def part2(inp):
    for i in range(13,len(inp)):
        if len(set(inp[i-13:i+1])) == 14:
            print(i+1)
            break
    
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