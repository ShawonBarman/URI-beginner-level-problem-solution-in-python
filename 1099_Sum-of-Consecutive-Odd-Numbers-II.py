N = int(input())
for i in range(N):
    x, y = input().split()
    x = int(x)
    y = int(y)
    sum=0
    if x<y:
        for i in range(x+1,y):
            if i%2!=0:
                sum+=i
    else:
        for i in range(y+1,x):
            if i%2!=0:
                sum+=i
    print(sum)