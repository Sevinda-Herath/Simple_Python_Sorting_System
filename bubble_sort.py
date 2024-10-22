import random

# Function bubble sort
def bubble_sort(arr):
    # Get the length of the array
    n = len(arr)

    # Go through all array elements
    for i in range(n):
        for j in range(0, n-i-1):
            # Swap if the element found is > than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__ == "__main__":

    # Array
    arr = [random.randint(1, 100) for _ in range(20)]

    # Print the unsorted array
    print("Unsorted array is:", arr)

    # Call the bubble sort function
    bubble_sort(arr)
    
    # Print the sorted array
    print("Bubble Sorted array is:", arr)
