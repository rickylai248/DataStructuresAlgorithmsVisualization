# Sorting Algorithm Visualizer
# Inspired throughout my completion in our Data Structures and Algorithm's course during university

# Beginning with sorting algorithms we learned first in-class which is inclusive of:
#   Selection Sort
#   Insertion Sort
#   Quick Sort
#   Merge Sort
# and more to come!

# OOP based implementation

import random, time

class Algorithm:
    def __init__(self, name):
        # constructor
        self.array = random.sample(range(512), 512)
        # Builtin Python function
        # returns a particular length list of items chosen from the sequence i.e. list, tuple, string or set. Used for random sampling without replacement.
        self.name = name

    def refreshScreen(self, swap1=None, swap2=None):
        import sorting_visualiser
        sorting_visualiser.update(self, swap1, swap2)
        # The update() method updates the dictionary with the elements from the another dictionary object or from an iterable of key/value pairs.

    def run(self):
        # runs the algorithm
        self.start_time = time.time()
        self.algorithm()
        time_elapsed = time.time() - self.start_time
        return self.array, time_elapsed

# Inspiration: https://www.youtube.com/watch?v=kFeXwkgnQ9U&ab_channel=DerrickSherrill

# https://www.geeksforgeeks.org/selection-sort/
# https://www.bigocheatsheet.com/
# https://en.wikipedia.org/wiki/Selection_sort
# "The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.
class SelectionSort(Algorithm):
    def __init__(self):
        super().__init__("SelectionSort")

    def algorithm(self):
        # traverse through all the elments in array
        for i in range(len(self.array)):
             # "Find the minimum element in remaining unsorted array"
            min_idx = i
            for j in range(i+1, len(self.array)):
                if self.array[j] < self.array[min_idx]:
                    min_idx = j
            # "Swap the found minimum element with the first element    ""  
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
            # update screen
            self.refreshScreen(self.array[i], self.array[min_idx])

# https://www.geeksforgeeks.org/insertion-sort/
# "Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.
class InsertionSort(Algorithm):
    def __init__(self):
        super().__init__("InsertionSort")

    def algorithm(self):
        # traverse entire length of array
        for i in range(len(self.array)):
            cursor = self.array[i]
            # "Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position"
            idx = i
            # set idx equal to i index
            while idx > 0 and self.array[idx-1] > cursor:
                self.array[idx] = self.array[idx-1]
                idx -= 1
            self.array[idx] = cursor
            # represents the key in this case 

            # refresh screen
            self.refreshScreen(self.array[idx], self.array[i])