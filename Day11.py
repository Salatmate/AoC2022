import sys
import aoc
test = '''Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1'''
file = open(sys.argv[0].split('\\')[-1].replace('py','txt'),'r')
raw_inp = file.read()
file.close()

def parseInput(inp):
    inp = aoc.cleanInput(inp,',-')
    inp = inp.split('\n\n') #split into lines
    #inp = [int(i) for i in inp] #convert each line into integer
    #inp = [[int(j) for j in i.split('\n')] for i in inp]
    inp = [i.split('\n') for i in inp] #convert each line into list
    #inp = [[int(j) for j in i.split(' ')] for i in inp] #convert each line into list
    return inp

inp = parseInput(raw_inp)
try: test = parseInput(test)
except Exception: pass

class monkey:
    def __init__(self,operation,test,iftrue,iffalse):
        self.operation = operation
        self.test = test
        self.iftrue = iftrue
        self.iffalse = iffalse
        self.inspected = 0
        
    def inspect(self,old,divide=False):
        self.inspected += 1
        new = eval(self.operation)
        if divide: new = new//3
        if new % self.test == 0:
            return new,self.iftrue
        else:
            return new,self.iffalse
        

from collections import defaultdict
def part1(inp):
    monkeys = []
    items = []
    for i in inp:
        items.append([int(i) for i in i[1].split(': ')[1].split()])
        old =5
        operation = i[2].split('= ')[1]
        test = int(i[3].split(' ')[-1])
        iftrue = int(i[4].split(' ')[-1])
        iffalse = int(i[5].split(' ')[-1])
        monkeys.append(monkey(operation,test,iftrue,iffalse))
    #print(items)
    for turns in range(20):
        for i in range(len(items)):
            while items[i]:
                worry,tossto = monkeys[i].inspect(items[i].pop(0),True)
                items[tossto].append(worry)
    ans = (sorted([monkeys[i].inspected for i in range(len(items))]))
    print(ans[-1]*ans[-2])
        

def part2(inp):
    monkeys = []
    items = []
    mod = 1
    for i in inp:
        items.append([int(i) for i in i[1].split(': ')[1].split()])
        old =5
        operation = i[2].split('= ')[1]
        test = int(i[3].split(' ')[-1])
        mod *= test
        iftrue = int(i[4].split(' ')[-1])
        iffalse = int(i[5].split(' ')[-1])
        monkeys.append(monkey(operation,test,iftrue,iffalse))
    for turns in range(10000):
        for i in range(len(items)):
            while items[i]:
                worry,tossto = monkeys[i].inspect(items[i].pop(0))
                items[tossto].append(worry%mod)
    #print([monkeys[i].inspected for i in range(len(items))])
    #print(items)
    ans = (sorted([monkeys[i].inspected for i in range(len(items))]))
    print(ans[-1]*ans[-2])
    
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
    s = time.time()
    part2(test)
    print(time.time()-s)
except Exception: pass