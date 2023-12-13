# def solution(n, stations, w):
#     answer = 0
#     temp = []
#     right = 0
#     for s in stations:
#         left = s-w
#         if right <= left:
#             temp.append(left-1-right)
#         right = s+w
#     if right < n:
#         temp.append(n-right)
#     pos = 2*w + 1
#     a = [i//pos+(1 if i%pos else 0) for i in temp]
#     return sum(a)
def solution(n, arr, w):
    bef=-w
    cnt=0
    ww=w*2+1
    for x in arr:
        cnt+=(x-bef-1)//ww
        bef=x
    return cnt+(n+w-bef)//ww