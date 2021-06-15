# Challenge Summary
<!-- Description of the challenge -->
Quick sort is similar to merge sort, in that it's a conquer and divide style sorting algorithm. It chooses a pivot value and partitions the input array into a left and right array. The main difference between merge sort and quick sort is that by the time quick sort has broken up the array into sub arrays of single elements the array is sorted.

Review the pseudocode of Quick sort, then trace the algorithm by stepping through the process with the provided sample array. Document your explanation by creating a blog article that shows the step-by-step output after each iteration through some sort of visual.
## Whiteboard Process
<!-- Embedded whiteboard image -->
![](../img/quick_sort.jpg)
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
- speed : bigO(n^2)
- space : bigO(n)

## Solution
<!-- Show how to run your code, and examples of it in action -->
test_list => [ 6,7,2,47,37,30 ]
quick_sort(test_list, 0, len(test_list) - 1)
test_list => [2, 6, 7, 30, 37, 47]
