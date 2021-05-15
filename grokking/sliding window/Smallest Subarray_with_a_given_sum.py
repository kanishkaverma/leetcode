import math

# O(N + N)
# sliding window solution


def smallest_subarray_with_given_sum_efficentk(s, arr):

    sum = 0
    length = math.inf
    start = 0
    for end in range(len(arr)):
        sum += arr[end]
        while sum >= s:
            length = min(length, end-start + 1)
            sum -= arr[start]
            start += 1
    if length == math.inf:

        return 0
    return length


def main():
    print(smallest_subarray_with_given_sum_efficentk(7, [2, 1, 5, 2, 3, 2]))
    print(smallest_subarray_with_given_sum_efficentk(7, [2, 1, 5, 2, 8]))


main()
