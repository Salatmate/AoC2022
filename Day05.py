import sys
test = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''
file = open(sys.argv[0].split('\\')[-1].replace('py','txt'),'r')
raw_inp = file.read()
file.close()

def parse(inp):
    inp = inp.split('\n\n') #split into lines
    #inp = [int(i) for i in inp] #convert each line into integer
    #inp = inp.split('\n\n')
    #inp = [[int(j) for j in i.split('\n')] for i in inp]
    #inp = [i.split(' ') for i in inp] #convert each line into list
    #inp = [[int(j) for j in i.split(' ')] for i in inp] #convert each line into list
    return inp

def adj4(pos):
    x,y = pos
    return [(x,y-1),(x-1,y),(x,y+1),(x+1,y)]
def adj8(pos):
    x,y = pos
    return [(x,y-1),(x-1,y-1),(x-1,y),(x-1,y+1),(x,y+1),(x+1,y+1),(x+1,y),(x+1,y-1)]

inp = parse(raw_inp)
try: test = parse(test)
except Exception: pass

def part1(inp):
    arr = [[] for i in range(9)]
    for i in inp[0].split('\n')[:-1]:
        i += ' '
        for j in range(0,len(i),4):
            if i[j+1] != ' ':
                arr[j//4] += [i[j+1]]
    for i in inp[1].split('\n'):
        line = i.split(' ')
        a = int(line[1])
        b = int(line[3])
        c = int(line[5])
        mov = []
        for j in range(a):
            mov.append(arr[b-1].pop(0))
        arr[c-1] = mov[::-1] + arr[c-1]
    print(''.join([i[0] for i in arr if i]))

def part2(inp):
    arr = [[] for i in range(9)]
    for i in inp[0].split('\n')[:-1]:
        i += ' '
        for j in range(0,len(i),4):
            if i[j+1] != ' ':
                arr[j//4] += [i[j+1]]
    for i in inp[1].split('\n'):
        line = i.split(' ')
        a = int(line[1])
        b = int(line[3])
        c = int(line[5])
        mov = []
        for j in range(a):
            mov.append(arr[b-1].pop(0))
        arr[c-1] = mov + arr[c-1]
    print(''.join([i[0] for i in arr if i]))
    
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