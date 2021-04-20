s1 = '5 1000'
s2 = '10 9 8 7 6'
s3 = '9 8 7 6 5'
##s2 = '2 3 1 4 3'
##s3 = '1 2 1 2 3'
#s1 = input()
#s2 = input()
#s3 = input()
n, x = map(int, s1.split())
A = list(map(int, s2.split()))
B = list(map(int, s3.split()))
# Вспомогательный список
# B[i][0] - масимальная цена продажи в этот день и позже
# B[i][1] - индекс дня с максимальной ценой продажи
B[-1] = (B[-1], -1)

for i in range(2,len(B)):
    if B[-i] > B[-i+1][0]:
        B[-i] = (B[-i], -i)
    else:
        B[-i] = B[-i+1]
 
a_mn = A[0]         # минимальная цена покупки не позже текущего дня
a_mni = 0           # индекс для с минимальной ценой покупки
mx = x              # максимальные деньги после покупки-продажи
mx_ij = (-1,-1)     # дни покупки и продажи, нумерация с 1

for i in range(len(A)-1):   # -1 потому, что покупать в последний день нельзя
    if A[i] < a_mn:
        a_mn = A[i]
        a_mni = i
    n_buy = x // a_mn                       # число купленных
    rest = x % a_mn                         # сдача
    x_sell = n_buy * B[i+1][0] + rest       # деньги после продажи в этот день
    if x_sell > mx:
        mx = x_sell
        mx_ij = (i+1, len(B) + B[i+1][1] +1)
 
print(mx)
print(*mx_ij)
