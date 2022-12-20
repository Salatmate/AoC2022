import sys
import aoc
test = '''Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.'''
file = open(sys.argv[0].split('\\')[-1].replace('py','txt'),'r')
raw_inp = file.read()
file.close()

def parseInput(inp):
    inp = aoc.cleanInput(inp,':abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.')
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
from math import ceil
def part1(inp):
    blueprints = {}
    for i in inp:
        bid, o1, c1, b1, b2, g1, g2 = [int(i) for i in i.split()]
        blueprints[bid] = [o1, c1, b1, b2, g1, g2]
    ans = 0
    for bid in blueprints:
        state = [(24,(0,0,0,0),(1,0,0,0))]
        o1, c1, b1, b2, g1, g2 = blueprints[bid]
        highest = 0
        while state:
            #input(state[-1]) if state[-1][0] >= 0 else 0
            time,resources,machines = state.pop(0)
            if resources[3] + time*(time-1)//2 < highest:
                continue
            if time <= 0: continue
            #print(bid,time,resources,machines)
            if highest < resources[3]:
                highest = resources[3]
                #print(highest)
            r1,r2,r3,r4 = resources
            m1,m2,m3,m4 = machines
            highest = max(highest,r4)
            flag = True
            if m1 >= 1 and m3 >= 1:
                buildtime = max(0,ceil((g1-r1)/m1),ceil((g2-r3)/m3))+1
                if buildtime == 1:
                    flag = False
                if (time-buildtime) > 0:
                    state.append((time-buildtime,(r1+m1*buildtime-g1,r2+m2*buildtime,r3+m3*buildtime-g2,r4+(time-buildtime)),(m1,m2,m3,m4+1)))
                    #print(time-buildtime)
            if flag:
                if m1 >= 1 and m2 >= 1 and time*g2 > r3+m3*time:
                    buildtime = max(0,ceil((b1-r1)/m1),ceil((b2-r2)/m2))+1
                    if (time-buildtime) > 0:
                        state.append((time-buildtime,(r1+m1*buildtime-b1,r2+m2*buildtime-b2,r3+m3*buildtime,r4),(m1,m2,m3+1,m4)))
                if m1 >= 1 and time*b2 > r2+m2*time:
                    buildtime = max(0,ceil((c1-r1)/m1))+1
                    if (time-buildtime) > 0:
                        state.append((time-buildtime,(r1+m1*buildtime-c1,r2+m2*buildtime,r3+m3*buildtime,r4),(m1,m2+1,m3,m4)))
                if 3 >= m1 >= 1:
                    buildtime = max(0,ceil((o1-r1)/m1))+1
                    if (time-buildtime) > 0:
                        state.append((time-buildtime,(r1+m1*buildtime-o1,r2+m2*buildtime,r3+m3*buildtime,r4),(m1+1,m2,m3,m4)))
        print(bid,highest*bid)
        ans += highest*bid
    print(ans)

def part2(inp):
    blueprints = {}
    for i in inp:
        bid, o1, c1, b1, b2, g1, g2 = [int(i) for i in i.split()]
        if bid <= 3: blueprints[bid] = [o1, c1, b1, b2, g1, g2]
    ans = 1
    for bid in blueprints:
        state = [(32,(0,0,0,0),(1,0,0,0))]
        o1, c1, b1, b2, g1, g2 = blueprints[bid]
        highest = 0
        while state:
            #input(state[-1]) if state[-1][0] >= 0 else 0
            time,resources,machines = state.pop(0)
            if resources[3] + time*(time-1)//2 < highest:
                continue
            if time <= 0: continue
            #print(bid,time,resources,machines)
            if highest < resources[3]:
                highest = resources[3]
                #print(highest)
            r1,r2,r3,r4 = resources
            m1,m2,m3,m4 = machines
            highest = max(highest,r4)
            flag = True
            if m1 >= 1 and m3 >= 1:
                buildtime = max(0,ceil((g1-r1)/m1),ceil((g2-r3)/m3))+1
                if buildtime == 1:
                    flag = False
                if (time-buildtime) > 0:
                    state.append((time-buildtime,(r1+m1*buildtime-g1,r2+m2*buildtime,r3+m3*buildtime-g2,r4+(time-buildtime)),(m1,m2,m3,m4+1)))
                    #print(time-buildtime)
            if flag:
                if m1 >= 1 and m2 >= 1 and time*g2 > r3+m3*time:
                    buildtime = max(0,ceil((b1-r1)/m1),ceil((b2-r2)/m2))+1
                    if (time-buildtime) > 0:
                        state.append((time-buildtime,(r1+m1*buildtime-b1,r2+m2*buildtime-b2,r3+m3*buildtime,r4),(m1,m2,m3+1,m4)))
                if m1 >= 1 and time*b2 > r2+m2*time:
                    buildtime = max(0,ceil((c1-r1)/m1))+1
                    if (time-buildtime) > 0:
                        state.append((time-buildtime,(r1+m1*buildtime-c1,r2+m2*buildtime,r3+m3*buildtime,r4),(m1,m2+1,m3,m4)))
                if 3 >= m1 >= 1:
                    buildtime = max(0,ceil((o1-r1)/m1))+1
                    if (time-buildtime) > 0:
                        state.append((time-buildtime,(r1+m1*buildtime-o1,r2+m2*buildtime,r3+m3*buildtime,r4),(m1+1,m2,m3,m4)))
        print(bid,highest)
        ans *= highest
    print(ans)
    
print('Part 1:')
part1(inp)
print('Part 1 Test:')
part1(test)
print('Part 2:')
part2(inp)
print('Part 2 Test:')
part2(test)