import sys
import aoc
test = '''1
2
-3
3
-2
0
4'''
fil = open(sys.argv[0].split('\\')[-1].replace('py','txt'),'r')
raw_inp = fil.read()
fil.close()

def parseInput(inp):
    inp = aoc.cleanInput(inp,',:')
    inp = inp.split('\n') #split into lines
    inp = [int(i) for i in inp] #convert each line into integer
    #inp = [[int(j) for j in i.split('\n')] for i in inp]
    #inp = [i.split(' ') for i in inp] #convert each line into list
    #inp = [[int(j) for j in i.split(' ')] for i in inp] #convert each line into list
    return inp

inp = parseInput(raw_inp)
try: test = parseInput(test)
except Exception: pass

from collections import deque
def part1(inp):
    fil = [i for i in range(len(inp))]
    for n,i in enumerate(inp):
        ind = fil.index(n)
        fil.pop(ind)
        newindex = (ind+i)%(len(inp)-1)
        fil = fil[:newindex] + [n] + fil[newindex:]
        #print(i,newindex,[inp[i] for i in fil])
    ind = 0
    fin = [inp[i] for i in fil]
    found = False
    n = 0
    ans = 0
    while True:
        if found: n += 1
        if fin[ind] == 0:
            found = True
        if n%1000 == 0 and n >= 1: 
            ans += fin[ind]
            print(n//1000,fin[ind])
        if n == 3000: break
        ind = (ind+1)%len(fin)
    print(ans)
def part2(inp):
    inp = [i*811589153 for i in inp]
    fil = [i for i in range(len(inp))]
    for mix in range(10):
        for n,i in enumerate(inp):
            ind = fil.index(n)
            fil.pop(ind)
            newindex = (ind+i)%(len(inp)-1)
            fil = fil[:newindex] + [n] + fil[newindex:]
            #print(i,newindex,[inp[i] for i in fil])
    ind = 0
    fin = [inp[i] for i in fil]
    found = False
    n = 0
    ans = 0
    while True:
        if found: n += 1
        if fin[ind] == 0:
            found = True
        if n%1000 == 0 and n >= 1: 
            ans += fin[ind]
            print(n//1000,fin[ind])
        if n == 3000: break
        ind = (ind+1)%len(fin)
    print(ans)
    
print('Part 1:')
part1(inp)
try:
    print('Part 1 Test:')
    part1(test)
except Exception: pass
print('Part 2:')
import time
s = time.time()
part2(inp)
print(time.time()-s)
try:
    print('Part 2 Test:')
    part2(test)
except Exception: pass