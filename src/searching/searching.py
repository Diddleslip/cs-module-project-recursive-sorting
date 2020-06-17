# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    low = start
    mid = 0
    high = end
    
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        # check if target is greater
        elif target > arr[mid]:
            low = mid + 1
            return binary_search(arr, target, low, end) ## ASK ABOUT IF WE NEED RETURNS OR WHEN TO USE
        # else target is less than mid
        else:
            high = mid - 1
            return binary_search(arr, target, low, high)

    return -1 # not found


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

