# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB) ## creates a number with same amount as arrA + arrB
    merged_arr = [0] * elements ## fills list with only 0's
    # index for arrA
    count1 = 0
    # index for arrB
    count2 = 0
    # index for merged_arr
    count3 = 0

    # Your code here
    # count3 will fill up to be merged's length once it's added every element from both arrays.
    while count3 != len(merged_arr):
        # if arrA and arrB still have material in them, go here.
        if count1 != len(arrA) and count2 != len(arrB):
            # if arrA[count1] is smaller than arrB[count2] add that to merged 
            if arrA[count1] <= arrB[count2]:
                # count3 tracks which index to replace in merged_arr
                merged_arr[count3] = arrA[count1]
                count1 += 1
                count3 += 1
            # if arrB[count2] is smaller than arrA[count1] add that to merged 
            else:
                # count3 tracks which index to replace in merged_arr
                merged_arr[count3] = arrB[count2]
                count2 += 1
                count3 += 1
        #else if count1 added all of its items, add the rest of count2's items
        elif count1 == len(arrA):
            # add all of arrB's items here
            merged_arr[count3] = arrB[count2]
            count2 += 1
            count3 += 1
        #else if count1 added all of its items, add the rest of count2's items
        else:
            # add all of arrA's items here
            merged_arr[count3] = arrA[count1]
            count1 += 1
            count3 += 1

    # print("YOYOYO", arrA, arrB)
    # print("THIS IS MERGED_ARR", merged_arr)
    return merged_arr

# arrA = [1, 1, 2, 3, 4]
# arrB = [4, 5, 6, 7]
# merge(arrA, arrB)

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        arr1 = arr[:len(arr) // 2] # splits the current arr into the first half,
        arr2 = arr[len(arr) // 2:] # splits the current arr into the second half,
        print("AYYE ", arr1)
        print("YOYOY ", arr2)
        return merge(merge_sort(arr1), merge_sort(arr2))
    # if len(arr) is at 1, then we can start joining them
    # else:
    #     merge(arr1, arr2)




    

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

