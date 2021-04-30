# Sorting Algorithm Visualizer
# Inspired throughout my completion in our Data Structures and Algorithm's course during university

# Beginning with sorting algorithms we learned first in-class which is inclusive of:
#   Selection Sort
#   Insertion Sort
#   Quick Sort
#   Merge Sort
# and more to come!

# Visualization tool created using Python to complement the sorting algorithmic construction file: See current work in progress above 
# Primarily for reference

import sortingalgorithm, time, os, sys
# https://docs.python.org/3/library/time.html
# https://www.geeksforgeeks.org/os-module-python-examples/ (important)
# https://www.python-course.eu/sys_module.php 
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
# captures mapping, represents string environment
import pygame
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame
# https://www.pygame.org/docs/ (custom effects, etc.)
# https://www.pygame.org/docs/tut/ImportInit.html
# https://docs.python.org/3/library/time.html
from pygame.locals import *
# imports the pygame module into the "pygame" namespace (saves typing)

# Inspiration: https://www.youtube.com/watch?v=kFeXwkgnQ9U&ab_channel=DerrickSherrill

dimensions = (1200, 600)
# able to change width, height
# warning: y value should fit array len

algorithms = {"SelectionSort": sortingalgorithm.SelectionSort(), \
              "InsertionSort": sortingalgorithm.InsertionSort()}
              # will add Merge, Heap, and Quick Sort in the near future
# https://www.geeksforgeeks.org/selection-sort/
# https://www.geeksforgeeks.org/insertion-sort/

if len(sys.argv) > 1:
    if sys.argv[1] == "list":
        for key in algorithms.keys(): print(key, end=" ")
        # returns a view object
        print("")
        sys.exit(0)

pygame.init()
# safely initalizes all imported pygame modules
display = pygame.display.set_mode((dimensions[0], dimensions[1]))
# https://www.pygame.org/docs/ref/display.html
display.fill(pygame.Color("white"))

def checkIfQuit():
    # check for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit();

def refresh(algorithm, swap1=None, swap2=None, display=display):
    display.fill(pygame.Color("white"))

    pygame.display.set_caption("Sorting Visualization Tool     Algorithm: {}     Time: {:.3f}      Status: Sorting".format(algorithm.name, time.time() - algorithm.start_time))
    k = int(dimensions[0]/len(algorithm.array))

    for i in range(len(algorithm.array)):
        colour = (0,0,0)
        if swap1 == algorithm.array[i]:
            colour = (0,255,0)
        elif swap2 == algorithm.array[i]:
            colour = (255,0,0)
        pygame.draw.rect(display, colour, (i*k,dimensions[1],k,-algorithm.array[i]))

    checkIfQuit()
    pygame.display.refresh()

def whileActive(algorithm, display, time):
    pygame.display.set_caption("Sorting Visualization Tool     Algorithm: {}     Time: {:.3f}      Status: Done".format(algorithm.name, time))

    while True:
        checkIfQuit()
        pygame.display.refresh()

def main():
    if len(sys.argv) < 2:
        print("Exception: Please enter a sorting algorithm")
    else:
        try:
            algorithm = algorithms[sys.argv[1]]
            try:
                time_elapsed = algorithm.run()[1]
                whileActive(algorithm, display, time_elapsed)
                pass
            except:
                pass
        except:
            # catch excepts
            print("Exception: {} is not one of the valid sorting algorithms".format(sys.argv[1]))
            print("Side Note: Sorting algorithms are in Camel Case format")

if __name__ == "__main__":
    main()