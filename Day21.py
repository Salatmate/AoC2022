import sys
import aoc
test = '''root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32'''
file = open(sys.argv[0].split('\\')[-1].replace('py','txt'),'r')
raw_inp = file.read()
file.close()

def parseInput(inp):
    inp = aoc.cleanInput(inp,',:')
    inp = inp.split('\n') #split into lines
    #inp = [int(i) for i in inp] #convert each line into integer
    #inp = [[int(j) for j in i.split('\n')] for i in inp]
    inp = [i.split() for i in inp] #convert each line into list
    #inp = [[int(j) for j in i.split(' ')] for i in inp] #convert each line into list
    return inp

inp = parseInput(raw_inp)
try: test = parseInput(test)
except Exception: pass

from collections import defaultdict
def part1(inp):
    monkeys = {}
    while inp:
        curr = inp.pop(0)
        if len(curr) == 2:
            monkeys[curr[0]] = curr[1]
        elif curr[1] not in monkeys or curr[3] not in monkeys:
            inp.append(curr)
        else:
            a = curr[1]
            b = curr[3]
            if curr[2] == '/': curr[2] = '//'
            monkeys[curr[0]] = str(eval(monkeys[a]+ curr[2] + monkeys[b]))
    print(monkeys['root'])

def part2(inp):
    monkeys = {}
    human = defaultdict(lambda:False)
    eqn = '@'
    while inp:
        curr = inp.pop(0)
        if len(curr) == 2:
            monkeys[curr[0]] = curr[1]
            if curr[0] == 'humn':
                human[curr[0]] = True
        elif curr[1] not in monkeys or curr[3] not in monkeys:
            inp.append(curr)
        else:
            a = curr[1]
            b = curr[3]
            if curr[2] == '/': curr[2] = '//'
            monkeys[curr[0]] = str(int(eval(monkeys[a]+ curr[2] + monkeys[b])))
            sign = {'+':'-','-':'+','*':'//','/':'*','//':'*'}
            if human[a] or human[b]:
                human[curr[0]] = True
            if curr[0] == 'root':
                if not human[a]: eqn = eqn.replace('@',monkeys[a])
                if not human[b]: eqn = eqn.replace('@',monkeys[b])
            elif human[a]:
                eqn = eqn.replace('@','(@)' + sign[curr[2]] + monkeys[b])
            elif human[b]:
                if curr[2] == '-':
                    eqn = eqn.replace('@',monkeys[a] + '-(@)')
                elif curr[2] == '//':
                    eqn = eqn.replace('@',monkeys[a] + '//(@)')
                else:
                    eqn = eqn.replace('@','(@)' + sign[curr[2]] + monkeys[a])
    print(eqn)
    print(eval(eqn))
    
print('Part 1:')
part1(inp[:])
print('Part 1 Test:')
part1(test[:])
print('Part 2:')
part2(inp[:])
print('Part 2 Test:')
part2(test[:])