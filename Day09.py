import sys
test = '''R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20'''
file = open(sys.argv[0].split('\\')[-1].replace('py','txt'),'r')
raw_inp = file.read()
file.close()

def cleanInput(inp,filter):
    for char in filter:
        inp = inp.replace(char,' ')
    return inp
def parseInput(inp):
    inp = cleanInput(inp,',-:')
    inp = inp.split('\n') #split into lines
    #inp = [int(i) for i in inp] #convert each line into integer
    #inp = [[int(j) for j in i.split('\n')] for i in inp]
    inp = [i.split(' ') for i in inp] #convert each line into list
    #inp = [[int(j) for j in i.split(' ')] for i in inp] #convert each line into list
    return inp

inp = parseInput(raw_inp)
try: test = parseInput(test)
except Exception: pass

def follow(hx,hy,tx,ty):
    if abs(hx-tx) == 2 and abs(hy-ty) == 2:
        tx += (hx-tx)//2
        ty += (hy-ty)//2
    if abs(hy-ty) == 2:
        tx = hx
        ty += (hy-ty)//2
    if abs(hx-tx) == 2:
        ty = hy
        tx += (hx-tx)//2
    return (tx,ty)

from collections import defaultdict
def part1(inp):
    hx,hy = (0,0)
    tx,ty = (0,0)
    visited = defaultdict(lambda:False)
    visited[(0,0)] = True
    for instr in inp:
        for i in range(int(instr[1])):
            if instr[0] == 'U': hy -= 1
            if instr[0] == 'L': hx -= 1
            if instr[0] == 'D': hy += 1
            if instr[0] == 'R': hx += 1
            tx,ty = follow(hx,hy,tx,ty)
            visited[(tx,ty)] = True
    print(list(visited.values()).count(True))

def part2(inp):
    pos = [(0,0) for i in range(10)]
    visited = defaultdict(lambda:False)
    visited[(0,0)] = True
    for instr in inp:
        for i in range(int(instr[1])):
            hx,hy = pos[0]
            if instr[0] == 'U': hy -= 1
            if instr[0] == 'L': hx -= 1
            if instr[0] == 'D': hy += 1
            if instr[0] == 'R': hx += 1
            pos[0] = (hx,hy)
            for j in range(1,10):
                hx,hy = pos[j-1]
                tx,ty = pos[j]
                pos[j] = follow(hx,hy,tx,ty)
            visited[pos[9]] = True
    print(list(visited.values()).count(True))
    
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