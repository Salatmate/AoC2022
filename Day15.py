import sys
import aoc
test = '''Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3'''
file = open(sys.argv[0].split('\\')[-1].replace('py','txt'),'r')
raw_inp = file.read()
file.close()

def parseInput(inp):
    inp = aoc.cleanInput(inp,',:=Sensoratclosestbeaconisatxy')
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
def part1(inp,y):
    ranges = []
    for i in inp:
        i = [int(i) for i in i.split()]
        sx,sy,ex,ey = i
        mh = aoc.manhattan(sx,sy,ex,ey)
        xspan = mh-abs(y-sy)
        if xspan >= 0: ranges += [(sx-xspan,sx+xspan)]
    ranges.sort()
    lx,hx = ranges[0]
    for i in ranges[1:]:
        hx = max(hx,i[1])
    print(hx-lx)
            
def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) // div
    y = det(d, ydiff) // div
    return x, y

def sign(x):
    if x > 0: return 1
    elif x < 0: return -1
    else: return 0
            
def part2(inp):
    sensors = []
    for i in inp:
        i = [int(i) for i in i.split()]
        sx,sy,ex,ey = i
        mh = aoc.manhattan(sx,sy,ex,ey)
        sensors.append((sx,sy,mh))
    sensors.sort()
    lines = []
    for i in range(len(sensors)):
        for j in range(i+1,len(sensors)):
            ax,ay,amh = sensors[i]
            bx,by,bmh = sensors[j]
            if (aoc.manhattan(ax,ay,bx,by) == amh+bmh+2):
                p1 = (ax+(amh+1)*sign(bx-ax),ay)
                p2 = (ax,ay+(amh+1)*sign(by-ay))
                lines += [(p1,p2)]
    for i in range(len(lines)):
        for j in range(i+1,len(lines)):
            x,y = (line_intersection(lines[i],lines[j]))
            print(x*4000000+y)
    
import time
print('Part 1:')
s = time.time()
part1(inp,2000000)
#print(time.time()-s)
print('Part 2:')
s = time.time()
part2(inp)
#print(time.time()-s)
