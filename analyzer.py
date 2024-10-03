# Import string data to search
import stringdata

# Import time module to record time
import time

def main():

    # Define tuple of words to search
    possible_words = stringdata.get_data()

    # Search for "not_here" linear
    start_time = time.time()
    linear_search(possible_words, "not_here")
    end_time = time.time()

    # Record time
    linear_search_word1_time = end_time - start_time


    # Search for "not_here" binary
    start_time = time.time()
    binary_search(possible_words, "not_here")
    end_time = time.time()

    # Record time
    binary_search_word1_time = end_time - start_time


    # Search for "mzzzz" linear
    start_time = time.time()
    linear_search(possible_words, "mzzzz")
    end_time = time.time()

    # Record time
    linear_search_word2_time = end_time - start_time

    # Search for "mzzzz" binary
    start_time = time.time()
    binary_search(possible_words, "mzzzz")
    end_time = time.time()

    # Record time
    binary_search_word2_time = end_time - start_time


    # Search for "aaaaa" linear
    start_time = time.time()
    linear_search(possible_words, "aaaaa")
    end_time = time.time()

    # Record time
    linear_search_word3_time = end_time - start_time

    # Search for "aaaaa" binary
    start_time = time.time()
    binary_search(possible_words, "aaaaa")
    end_time = time.time()

    # Record time
    binary_search_word3_time = end_time - start_time

    # Display times
    print("Linear search for 'not_here': " + str(linear_search_word1_time))
    print("Binary search for 'not_here': " + str(binary_search_word1_time))
    print("Linear search for 'mzzzz': " + str(linear_search_word2_time))
    print("Binary search for 'mzzzz': " + str(binary_search_word2_time))
    print("Linear search for 'aaaaa': " + str(linear_search_word3_time))
    print("Binary search for 'aaaaa': " + str(binary_search_word3_time))


# Linear search algorithm
def linear_search(container: tuple[str], element: str) -> int:

    # Iterate through every element in the tuple
    for index in range(len(container)):
        if container[index] == element:
            # Return index if the desired element is found
            return index

    # Return -1 if the desired element is not found after iterating through the entire tuple
    return -1


# Binary search algorithm
def binary_search(container: tuple[str], element: str) -> int:

    # Declare index variables for binary search
    low_end = 0
    high_end = len(container) - 1

    # While there are still elements in the tuple constantly cut the tuple in half, based on the
    # middle index until element is found.
    # This reduces the tuple to search by half each iteration.
    while low_end <= high_end:

        # Find the middle index in the tuple
        mid = (low_end + high_end) // 2

        # If middle index is the element, return the index
        if container[mid] == element:
            return mid

        # If the middle index is less than the element, make the lower end of the tuple the middle index
        elif container[mid] < element:
            low_end = mid + 1

        # If the middle index is greater than the element, make the higher end of the tuple the middle index
        else:
            high_end = mid - 1

    # Return -1 if element is not found after binary search
    return -1


# Method to run program
if __name__ == '__main__':
    main()