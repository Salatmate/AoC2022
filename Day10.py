import sys
test = '''addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop'''
file = open(sys.argv[0].split('\\')[-1].replace('py','txt'),'r')
raw_inp = file.read()
file.close()

def visual(grid):
    output = ''
    positions = list(grid.keys())
    for y in range(min(positions,key=lambda x:x[1])[1],max(positions,key=lambda x:x[1])[1]+1):
            for x in range(min(positions,key=lambda x:x[0])[0],max(positions,key=lambda x:x[0])[0]+1):
                if grid[(x,y)]: output += '██'
                else: output += '  '
            output += '\n'
    print(output)

def cleanInput(inp,filter):
    for char in filter:
        inp = inp.replace(char,' ')
    return inp
def parseInput(inp):
    inp = cleanInput(inp,',:')
    inp = inp.split('\n') #split into lines
    #inp = [int(i) for i in inp] #convert each line into integer
    #inp = [[int(j) for j in i.split('\n')] for i in inp]
    inp = [i.split(' ') for i in inp] #convert each line into list
    #inp = [[int(j) for j in i.split(' ')] for i in inp] #convert each line into list
    return inp

inp = parseInput(raw_inp)
try: test = parseInput(test)
except Exception: pass

from collections import defaultdict
def part1(inp):
    reg = 1
    index = 0
    cycle = 1
    start = -100
    ans = 0
    while index < len(inp):
        #print(cycle,inp[index], reg)
        if inp[index][0] == 'noop':
            cycle += 1
            index += 1
        elif start != cycle-1:
            start = cycle
            cycle += 1
        else:
            reg += int(inp[index][1])
            cycle += 1
            index += 1
            start = -100
        if (cycle-20)%40 == 0 and cycle <= 220:
            ans += cycle*reg
    print(ans)

def part2(inp):
    reg = 1
    index = 0
    cycle = 1
    start = -100
    ans = 0
    grid = defaultdict(lambda:False)
    while index < len(inp):
        #print(cycle,inp[index], reg)
        if reg-1 <= (cycle-1)%40 <= reg+1:
            grid[((cycle-1)%40,(cycle-1)//40)] = True
        if inp[index][0] == 'noop':
            cycle += 1
            index += 1
        elif start != cycle-1:
            start = cycle
            cycle += 1
        else:
            reg += int(inp[index][1])
            cycle += 1
            index += 1
            start = -100
    visual(grid)
    
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