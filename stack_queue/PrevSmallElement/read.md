# Previous Smaller Element

## Problem Statement
What will be the previous smaller element for a given index in an array

## Solution 1: Bruteforce
Loop through each one to compare and put

## Solution 2: Using Stack
Using a monotonic Stack (increasing order)

### Approach
The Approach is the same as Next Greater Element only the conditions are changed
1. We gonna start the array from the left hand side
2. the pop part will now be stack[-1]>= arr[i]


### Complexity Analysis
- **Time Complexity**: **O(2N)** where n is the length of the inpurt array.
- **Space Complexity**: **O(N)+O(N)** (worst is it will pop will elements)