a,b = map(int, input().split())
c,d = map(int, input().split())

#사과 합, 오렌지 합를 비교하여 낮은 것을 옮긴다.
if(a+d >= b+c):
    #사과가 많으면 오렌지를 옮긴다.
    print(b+c)
else:
    #오렌지가 많으면 사과를 옮긴다.
    print(a+d)