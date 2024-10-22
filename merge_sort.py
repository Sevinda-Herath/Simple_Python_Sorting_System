import random

# Function merge sort
def merge_sort(arr):
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr)//2 
        # Dividing the array elements into 2 halves
        L = arr[:mid]      
        R = arr[mid:]      

        # Sorting the first half
        merge_sort(L) 
        # Sorting the second half
        merge_sort(R)  

        i = j = k = 0

        # Copy data to arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

if __name__ == "__main__":

    # Array
    arr = [random.randint(1, 100) for _ in range(20)]

    # Print the unsorted array
    print("Unsorted array is:", arr)

    # Call the bubble sort function
    merge_sort(arr)
    
    
    # Print the sorted array
    print("Merge Sorted array is:", arr)
