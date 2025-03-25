# JimmySort
This is a sorting algorithm which came to me in a dream.
It took until after I wrote it down to realize I had invented
Quick Sort but worse in almost every way. Still, I invented
my own sorting algorithm.

### Instructions
run `python3 jimmysort.py` in the project directory. This generates
tests and runs them, and prints the P/F result

## Time Complexity
This runs in worst cast O(n^2) when the pivot is the smallest
or largest element in the list, like quicksort.

Best and average case it is O(nlgn) because the list can be
split almost perfectly in halves lgn times, and then the
iteration left-right sorting loop takes O(n) time in each of
these subproblems

Using a pivot selection algo keeps it away from O(n^2)

## Memory
There are n lists of 1 element at the lowest level, and the
recusion stack is of size O(lgn) frames best case, and O(n)
frames worst case. This yields O(n) space. 

Its also worth noting that this is not in-place, and the pop
for the pivot means the original list is corrupted. It is also
not stable. So, basically quick sort but just worse. lol.