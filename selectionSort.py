def selection_sort(arr):
    # take total length of an array
    n = len(arr)
    #Loop 01 
    for i in range(n-1):
        min_idx = i
        #Loop 02
        for j in range(i+1,n):
            if arr[j]< arr[min_idx]:
                min_idx=j
        arr[i] , arr[min_idx] = arr[min_idx], arr[i]

def print_values(arr):
    for val in arr:
        print(val,end=" ")
    print()




if __name__ == "__main__":
    arr = [6,4,2,0,7,5,9]

    print("Array before Sorting : ", end=" ")
    print_values(arr)

    selection_sort(arr)

    print("Array after Sorting : ", end= " ")
    print_values(arr)

