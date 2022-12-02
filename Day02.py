import sys
test = '''A Y
B X
C Z'''
file = open(sys.argv[0].split('\\')[-1].replace('py','txt'),'r')
raw_inp = file.read()
file.close()

def parse(inp):
    inp = inp.split('\n') #split into lines
    #inp = [int(i) for i in inp] #convert each line into integer
    #inp = inp.split('\n\n')
    #inp = [[int(j) for j in i.split('\n')] for i in inp]
    inp = [i.split(' ') for i in inp] #convert each line into list
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
    for x,y in inp:
        if y == 'X':  ans += 1
        if y == 'Y': ans += 2
        if y == 'Z': ans += 3
        if (x == 'A' and y == 'X') or (x == 'B' and y == 'Y') or (x == 'C' and y == 'Z'): ans += 3
        if x == 'A' and y== 'Y': ans += 6
        elif x == 'B' and y== 'Z': ans += 6
        elif x == 'C' and y== 'X': ans += 6
        else: ans += 0
        
    print(ans)

def part2(inp):
    ans = 0
    for x,y in inp:
        if y == 'X': 
            ans += 0
            if x == 'A': ans += 3
            if x == 'B': ans += 1
            if x == 'C': ans += 2
        if y == 'Y': 
            ans += 3
            if x == 'A': ans += 1
            if x == 'B': ans += 2
            if x == 'C': ans += 3
        if y == 'Z': 
            ans += 6
            if x == 'A': ans += 2
            if x == 'B': ans += 3
            if x == 'C': ans += 1
        
        else: ans += 0
    print(ans)
    
print('Part 1:')
part1(inp)
part1(test)
print('Part 2:')
part2(inp)
part2(test)