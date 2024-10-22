# Please Change "genarate_dataset" value to your liking
# to change genarated number count.

import random
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
import timeit

def generate_dataset(size):
    return [random.randint(1, 10000000) for _ in range(size)]

def sort_data(dataset, algorithm, order):
    start_time = timeit.default_timer()
    if algorithm == "bubble":
        bubble_sort(dataset)
    elif algorithm == "insertion":
        insertion_sort(dataset)
    elif algorithm == "merge":
        merge_sort(dataset)
    
    if order == "desc":
        dataset.reverse()
    end_time = timeit.default_timer()
    return end_time - start_time

if __name__ == "__main__":
    dataset = generate_dataset(1000) # <---- Here
    
    print("Dataset generated successfully.")
    
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

    time_taken = sort_data(dataset, algorithm, order)

    print(f"Sorted data using {algorithm} algorithm in {order} order")
    print(f"Time taken to sort: {time_taken} seconds")
