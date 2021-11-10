ins = []
#x = 1
for i in range(4):
    q = [int(i) for i in input().split()]
    ins+=(q[:])
    #x*=-1

x = [1, 2, 3, 4, 8, 7, 6, 5, 9, 10, 11, 12, 15, 14, 13]
def ch(x):
    answer = 1
    for i in x:
        for j in x[x.index(i):]:
            if i > j:
                answer *= -1
    return answer

if ch(ins)==ch(x):
    print('Бинго!')
else:
    print('Не повезло...')