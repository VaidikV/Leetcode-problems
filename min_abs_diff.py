
def minimumAbsDifference(arr):
    arr.sort()
    min_diff = float('inf')
    for i in range(1, len(arr)):
        min_diff = min(min_diff, arr[i] - arr[i-1])

    result = []
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] == min_diff:
            result.append([arr[i-1], arr[i]])

    return result

arr = [4,2,1,3]
print(minimumAbsDifference(arr))
