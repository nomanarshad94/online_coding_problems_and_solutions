# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
pb = dict()
for i in range(n):
    name, number = input().split(' ')
    pb[name] = int(number)

while True:
    try:
        name = input()
    except:
        break
    if name in pb.keys():
        print(name + "=" + str(pb[name]))
    else:
        print('Not found')
