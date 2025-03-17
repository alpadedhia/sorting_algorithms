# Bubble Sort

## Overview
Bubble Sort is a simple comparison-based sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process continues until the list is sorted.

## Algorithm Steps
1. Start with an unsorted array of size `n`.
2. Iterate through the array and compare adjacent elements.
3. Swap elements if they are in the wrong order.
4. Continue the process for `n-1` passes, reducing the range each time.
5. If no swaps are made in a pass, the array is already sorted.

## Complexity Analysis
- **Time Complexity:**
  - Best Case: O(n) (when already sorted)
  - Average Case: O(n²)
  - Worst Case: O(n²)
- **Space Complexity:** O(1) (in-place sorting)
- **Stable?** Yes (preserves relative order of equal elements)

## Key Points
- Simple but inefficient for large datasets.
- Performs well when the array is already nearly sorted.
- Requires multiple passes even if only a few elements are out of place.
- Used in educational contexts to demonstrate sorting concepts.
