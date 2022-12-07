import sys
test = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''
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
        inp = inp.replace(char,'')
    return inp
def parseInput(inp):
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
    ans = 0
    directory = '/'
    system = defaultdict(list)
    filesize = {}
    for i in inp:
        i = i.split(' ')
        if i[0] == '$' and i[1] == 'cd':
            if i[2] == '/': directory = '/'
            elif i[2] == '..': directory = '-'.join(directory.split('-')[:-1])
            else: directory += '-' + i[2]
        elif i[0] != '$':
            if i[0] == 'dir': 
                system[directory].append(directory + '-' + i[1])
            else:
                system[directory].append(directory + '-' + i[1])
                filesize[directory + '-' + i[1]] = int(i[0])
    dirsize = defaultdict(lambda:0)
    for directory in system:
        while system[directory]:
            currdir = system[directory].pop(0)
            if currdir in filesize:
                dirsize[directory] += filesize[currdir]
            else:
                system[directory] += system[currdir]
    ans = 0
    for i in dirsize:
        if dirsize[i] <= 100000: ans += dirsize[i]
    print('Part 1')
    print(ans)
    free = 30000000-(70000000-dirsize['/'])
    print('Part 2')
    for i in sorted(list(dirsize.keys()),key=lambda x:dirsize[x]):
        if dirsize[i] >= free:
            print(dirsize[i])
            break
    

print('Input:')
part1(inp)
try:
    print('Test:')
    part1(test)
except Exception: pass