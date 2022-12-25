file = open('Day25.txt','r')
inp = file.read()
file.close()

test = '''1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122'''

def parse(i):
    i = i.split('\n')
    return i

test = parse(test)
inp = parse(inp)

def part1(inp):
    num = 0
    for i in inp:
        i = list(i)
        for x in range(len(i)):
            w = len(i)-x-1
            if i[w] == '-': num += 5**x * -1
            elif i[w] == '=': num += 5**x * -2
            else: num += 5**x * int(i[w])
    print(num)
    sna = []
    while num:
        sna = [num % 5] + sna
        num //= 5
    sna = [0] + sna
    for i in reversed(range(1,len(sna))):
        if sna[i] >= 3:
            sna[i] -= 5
            sna[i-1] += 1
    sna = ''.join([str(i) for i in sna])
    sna = sna.replace('-2','=').replace('-1','-')
    if sna[0] == '0': print(sna[1:])
    else: print(sna)
            

part1(test)
part1(inp)