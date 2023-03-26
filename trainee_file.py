arr1 = [2, 4, 6, 8]
arr2 = [1, 3, 5, 7, 9]
summ_arr = arr1 + arr2
print(summ_arr)
sort_arr = []
while summ_arr:
    minimum = summ_arr[0]
    for j in summ_arr:
        if j < minimum:
            minimum = j
    sort_arr.append(minimum)
    summ_arr.remove(minimum)
print(sort_arr)
