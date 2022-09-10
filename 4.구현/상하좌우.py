n = int(input())
gogo = list(input().split())

nx = [0, 0, -1, 1]
ny = [1, -1, 0, 0]
go = ['D', 'U', 'L', 'R']                                       # UP인 경우 -1,0 유의하기

x = y = 1
for i in gogo:
    sunseo = go.index(i)
    if n >= x + nx[sunseo] >= 1 and n >= y + ny[sunseo] >= 1:   #지도 안에 있으면 가기
        x = x + nx[sunseo]
        y = y + ny[sunseo]
    
print(str(y)+' '+str(x))