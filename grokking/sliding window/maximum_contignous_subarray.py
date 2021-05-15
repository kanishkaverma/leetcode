# O(n*k) ; not efficient


def maximum_contignous_subarray_brute(arr, k):
    max = -1
    for i in range(len(arr)-k + 1):
        sum = 0
        for j in range(i, i+k):
            sum += arr[j]
        if sum > max:
            max = sum
    return max

# O(n) ; efficient ; sliding window


def maximum_contingnous_subarray_efficient(arr, k):
    res = 0
    start, sum = 0, 0
    for end in range(len(arr)):
        sum += arr[end]
        if end >= k-1:
            res = max(res, sum)
            sum -= arr[start]
            start += 1
    return res


def main():
    print(maximum_contignous_subarray_brute([2, 1, 5, 1, 3, 2], 3))
    print(maximum_contignous_subarray_brute([2, 3, 4, 1, 5], 2))

    print(maximum_contingnous_subarray_efficient([2, 1, 5, 1, 3, 2], 3))
    print(maximum_contingnous_subarray_efficient([2, 3, 4, 1, 5], 2))


main()
