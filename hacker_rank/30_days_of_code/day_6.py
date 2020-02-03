# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())

for i in range(t):
    s = input()
    l = len(s)
    s_arr = []
    s_arr_odd = []
    for j in range(l):
        if j % 2 == 0:
            s_arr.append(s[j])
        else:
            s_arr_odd.append(s[j])
    print(''.join(s_arr) + ' ' + ''.join(s_arr_odd))
