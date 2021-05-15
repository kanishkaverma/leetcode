def mergesort(low, high): 
    mid = low+high//2 
    if low<high:
        mergesort(low, mid)
        mergesort(mid+1, high) 
        merge(low,  high)


# def merge(low, mid, high): 
def merge(left, right):
    """Merge sort merging function."""

    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result

def test(): 

    list1 = [3,5,6,7,8,9]
    print(mergesort(list1[0], list[len(list1)-1]))
    print(list1)