# Selection Sort

## Overview
Selection Sort is a simple comparison-based sorting algorithm. It divides the input array into a sorted and an unsorted region. The algorithm repeatedly selects the smallest (or largest) element from the unsorted section and swaps it with the leftmost unsorted element, expanding the sorted portion.

## Algorithm Steps
1. Start with an unsorted array of size `n`.
2. Iterate from index `0` to `n-1`.
3. Find the minimum element in the unsorted part.
4. Swap it with the first unsorted element.
5. Repeat until the array is sorted.

## Complexity Analysis
- **Time Complexity:**
  - Best Case: O(n²)
  - Average Case: O(n²)
  - Worst Case: O(n²)
- **Space Complexity:** O(1) (in-place sorting)
- **Stable?** No (swapping can disrupt relative order of equal elements)

## Key Points
- Works well for small datasets but inefficient for large datasets.
- Does not require extra memory.
- Performs poorly compared to advanced sorting algorithms like QuickSort and MergeSort.
- Can be useful when swaps are expensive compared to comparisons.
