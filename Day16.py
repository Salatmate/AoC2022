import sys
import aoc
test = '''Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II'''
file = open(sys.argv[0].split('\\')[-1].replace('py','txt'),'r')
raw_inp = file.read()
file.close()

def parseInput(inp):
    inp = aoc.cleanInput(inp,',:;')
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
    adjs = {}
    rates = {}
    prio = []
    for i in inp:
        i = i.split()
        v = i[1]
        rate = int(i[4].replace('rate=',''))
        adjs[v] = i[9:]
        if rate > 0:
            prio.append(v)
            rates[v] = rate
    dist = defaultdict(lambda:1000000)
    for start in prio:
        paths = [(0,start)]
        visited = set()
        while paths:
            time,v = paths.pop(0)
            visited.add(v)
            dist[(start,v)] = time 
            for adj in adjs[v]:
                if adj not in visited and dist[(start,adj)] > time:
                    paths.append((time+1,adj))
    paths = [(30,0,'AA',prio)]
    ans = 0
    while paths:
        time,pressure,curr,remaining = paths.pop(0)
        ans = max(ans,pressure)
        for adj in remaining:
            if time - dist[(adj,curr)] > 1:
                newtime = time-dist[(adj,curr)]-1
                newpressure = pressure + rates[adj]*newtime
                paths.append((newtime,newpressure,adj,[i for i in remaining if i != adj]))
        
    print(ans)
        
def part2(inp):
    adjs = {}
    rates = {}
    prio = []
    nodes = []
    for i in inp:
        i = i.split()
        v = i[1]
        rate = int(i[4].replace('rate=',''))
        adjs[v] = i[9:]
        nodes.append(v)
        if rate > 0:
            prio.append(v)
            rates[v] = rate
    dist = {}
    for start in prio:
        paths = [(0,start)]
        visited = set()
        while paths:
            d,curr = paths.pop(0)
            if curr in visited: continue
            visited.add(curr)
            dist[(start,curr)] = d
            for adj in adjs[curr]:
                if adj not in visited:
                    paths.append((d+1,adj))
        
    paths = [(26,0,'AA',prio)]
    best = defaultdict(lambda:0)
    partitions = []
    while paths:
        time,pressure,curr,remaining = paths.pop(0)
        closed = tuple([i for i in prio if i not in remaining])
        if best[closed] < pressure:
            best[closed] = pressure
            partitions.append(closed)
        for adj in remaining:
            newtime = time-dist[(adj,curr)]-1
            if newtime > 0:
                newpressure = pressure + newtime*rates[adj]
                newremaining = [i for i in remaining if i != adj]
                paths.append((newtime,newpressure,adj,newremaining))
    partitions.sort(key=lambda x:best[x],reverse=True)
    ans = 0
    for i in partitions:
        for j in partitions:
            if not set(i)&set(j) and ans < best[i]+best[j]: 
                ans = best[i]+best[j]
        if best[i] < ans//2:
            break
    print(ans)
    
import time
print('Part 1:')
s = time.time()
part1(inp)
#print(time.time()-s)
print('Part 1 Test:')
part1(test)
print('Part 2:')
s = time.time()
part2(inp)
#print(time.time()-s)

print('Part 2 Test:')
part2(test)