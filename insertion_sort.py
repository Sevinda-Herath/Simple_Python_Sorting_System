import random

# Function insertion sort
def insertion_sort(arr):

    # Go through 1 to len(arr)
    for i in range(1, len(arr)):
        # Create Key element
        key = arr[i]

        j = i-1
        # Move elements of arr[0..i-1] that > key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # Place the Key at its correct position
        arr[j + 1] = key

if __name__ == "__main__":
    
    # Array
    arr = [random.randint(1, 100) for _ in range(20)]

    # Print the unsorted array
    print("Unsorted array is:", arr)

    # Call the bubble sort function
    insertion_sort(arr)
    
    
    # Print the sorted array
    print("Insertion Sorted array is:", arr)
