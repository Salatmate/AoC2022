import sys
test = ''''''
file = open(sys.argv[0].split('\\')[-1].replace('py','txt'),'r')
raw_inp = file.read()
file.close()

def parse(inp):
    #inp = inp.split('\n')
    #inp = [int(i) for i in inp]
    inp = inp.split('\n\n')
    inp = [[int(j) for j in i.split('\n')] for i in inp]
    #inp = [tuple([int(j) for j in i.split(' ')]) for i in inp]
    return inp

inp = parse(raw_inp)
try:
    test = parse(test)
except Exception:
    pass

def part1(inp):
    print(max([sum(i) for i in inp]))

def part2(inp):
    print(sum(sorted([sum(i) for i in inp])[-3:]))
    
print('Part 1:')
part1(inp)
print('Part 2:')
part2(inp)