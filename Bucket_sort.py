def bucket_sort(arr):
    if len(arr) == 0:
        return arr
    
    # Determine the range of values in the array
    min_val = min(arr)
    max_val = max(arr)
    num_buckets = max_val - min_val + 1
    
    # Create empty buckets
    buckets = [[] for _ in range(num_buckets)]
    
    # Distribute elements into buckets
    for num in arr:
        index = num - min_val
        buckets[index].append(num)
    
    # Sort each bucket using another sorting algorithm (e.g., insertion sort)
    for bucket in buckets:
        insertion_sort(bucket)
    
    # Concatenate sorted buckets
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)
    
    return sorted_array

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage
input_array = [3, 6, 8, 10, 1, 2, 1]
sorted_array = bucket_sort(input_array)
print(sorted_array)
