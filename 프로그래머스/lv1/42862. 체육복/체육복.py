def solution(n, lost, reserve):
    answer = 0
    arr = [1] * n
    for i in lost:
        arr[i - 1] -= 1
    for i in reserve:
        arr[i - 1] += 1

    for i in range(n):
        if arr[i] == 0:
            if i > 0 and arr[i - 1] == 2:
                arr[i] += 1
                arr[i - 1] -= 1
            elif i < n - 1 and arr[i + 1] == 2:
                arr[i] += 1
                arr[i + 1] -= 1

    return sum([bool(i) for i in arr])
