N = int(input())
C = 0
R = 0
S = 0
for i in range(N):
    num, txt = input().split()
    if txt == "C":
        C += int(num)
    if txt == "R":
        R += int(num)
    if txt == "S":
        S += int(num)
total = C+R+S
print("Total: {} cobaias".format(total))
print("Total de coelhos: {}".format(C))
print("Total de ratos: {}".format(R))
print("Total de sapos: {}".format(S))
print("Percentual de coelhos: {0:.2f} %".format((C/total)*100))
print("Percentual de ratos: {0:.2f} %".format((R/total)*100))
print("Percentual de sapos: {0:.2f} %".format((S/total)*100))
