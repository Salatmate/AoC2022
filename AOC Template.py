import sys
test = ''''''
file = open(sys.argv[0].split('\\')[-1].replace('py','txt'),'r')
raw_inp = file.read()
file.close()

def parse(inp):
    inp = inp.split('\n') #split into lines
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
    ans = 0
    print(ans)

def part2(inp):
    ans = 0
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
