# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    n=int(input())
    if n ==1:
        print('Not prime')
    elif n==2:
        print('Prime')
    else:
        flag=False
        for j in range(2,round(n**(1/2))+1):
            if n%j==0:
                print('Not prime')
                flag=False
                break
            else:
                flag=True
        if flag:
            print('Prime')
               
