import random
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort

def generate_dataset(size):
    return [random.randint(1, 1000) for _ in range(size)]

def sort_data(dataset, algorithm, order):
    if algorithm == "bubble":
        bubble_sort(dataset)
    elif algorithm == "insertion":
        insertion_sort(dataset)
    elif algorithm == "merge":
        merge_sort(dataset)
    
    if order == "desc":
        dataset.reverse()
    
if __name__ == "__main__":
    dataset = generate_dataset(100)
         
    print("Dataset generated successfully.")
    print("Unsorted dataset:")
    print(dataset)
    
    print("Select a sorting algorithm:")
    print("1. Bubble Sort")
    print("2. Insertion Sort")
    print("3. Merge Sort")
    
    while True:
        choice = input("Enter your choice (1/2/3): ")
        if choice in ["1", "2", "3"]:
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    algorithm = ""
    if choice == "1":
        algorithm = "bubble"
    elif choice == "2":
        algorithm = "insertion"
    elif choice == "3":
        algorithm = "merge"

    while True:
        order = input("Do you want the data to be sorted in ascending (asc) or descending (desc) order? (asc/desc): ").lower()
        if order in ["asc", "desc"]:
            break
        else:
            print("Invalid choice. Please enter 'asc' or 'desc'.")

    sort_data(dataset, algorithm, order)

    print(f"Sorted data using {algorithm} algorithm in {order} order:")
    print(dataset)
