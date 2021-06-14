Selection Sort is a sorting algorithm that traverses the array multiple times as it slowly builds out the sorting sequence. The traversal keeps track of the minimum value and places it in the front of the array which should be incrementally sorted.

        Pseudocode
        SelectionSort(int[] arr)
            DECLARE n <-- arr.Length;
            FOR i = 0; i to n - 1
                DECLARE min <-- i;
                FOR j = i + 1 to n
                    if (arr[j] < arr[min])
                        min <-- j;

                DECLARE temp <-- arr[min];
                arr[min] <-- arr[i];
                arr[i] <-- temp;
## Trace

Sample Array: [8,4,23,42,16,15]

Pass 1:

Pass 1 of Selection Sort

In the first pass through of the selection sort, we evaluate if there is a smaller number in the array than what is currently present in index 0. We find this smaller number right away in index 1. The minimum value gets updated to remember this index. At the end of the evaluation, the smaller number will be swapped with the current value in index i. This results in our smallest number of our array being placed first.

![](../img/blog/pass1.jpg)
Pass 2:

Pass 2 of Selection Sort

The second pass through the array evaluates the remaining values in the array to see if there is a smaller value other than the current position of i. 8 is the 2nd smallest number in the array, so it “swaps” with itself. The minimum value does not change at all during the iteration of this pass.

![](../img/blog/pass2.jpg)

Pass 3:

Pass 3 of Selection Sort

The third pass through evaluates the remaining indexes in the array, starting at position 2. Both position 4 and 5 are smaller than the value in position 2. Each time a smaller number than the current minimum is found, the variable will update to the new smallest number. In this case, 15 is the next smallest number. As a result, it will swap with position 2.
![](../img/blog/pass3.jpg)

Pass 4:

Pass 4 of Selection Sort

The 4th pass through on the array proves that 16 is the next smallest number in the array, and as a result, switches places with the 42.

![](../img/blog/pass4.jpg)

Pass 5:

Pass 5 of Selection Sort

The 5th pass through of the array only has one other index to evaluate. Since the last index value is larger than index 4, the two values will swap.

![](../img/blog/pass5.jpg)

Pass 6:

Pass 6 of Selectio Sort

On its final iteratation through the array, it will swap places with itself as it evaluates the value against itself.

After this iteration, i will increment to 6, forcing it to break out of the outer for loop and leaving our array now sorted.

![](../img/blog/pass6.jpg)


## Efficency

Time: O(n^2)
The basic operation of this algorithm is comparison. This will happen n * (n-1) number of times…concluding the algorithm to be n squared.
Space: O(1)
No additional space is being created. This array is being sorted in place…keeping the space at constant O(1).
