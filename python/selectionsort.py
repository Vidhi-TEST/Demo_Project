def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Test the selection sort function
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print(sorted_arr)


if __name__ == "__main__":
    data = [64, 25, 12, 22, 11]
    print("Unsorted array:", data)
    selection_sort(data)
    print("Sorted array:", data)
