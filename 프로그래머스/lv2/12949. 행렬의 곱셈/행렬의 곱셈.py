def solution(arr1, arr2):
    answer = []
    a, x, b = len(arr1), len(arr2), len(arr2[0])
    for i in arr1:
        print(i)
    print('------------')
    for i in arr2:
        print(i)
    for i in range(a): 
        temp_arr = []
        for j in range(b): 
            temp = 0
            for k in range(x): 
                # print(arr1[i][k])
                # print(arr2[k][j])
                temp += arr1[i][k]*arr2[k][j]
            temp_arr.append(temp)
        answer.append(temp_arr)
    return answer