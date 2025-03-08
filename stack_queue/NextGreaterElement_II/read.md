# Next Greater Element II

## Problem Statement
What will be the next greater element for a given index in an array 
Note -  if not present in right then circle back to first

## Solution 1: Bruteforce 
Same O(N^2) with space complexity O(N)

## Solution 2: Using Stack
The approach is still using monotonic Stack

### Approach
1. The function uses a monotonic decreasing stack to efficiently determine the next greater element.

2. It iterates over the array twice (simulating a circular array) to ensure all elements have a chance to find their next greater element.

### Complexity Analysis
 - **Time Complexity**: **O(n)** where n is the length of the input array.
 - **Space Complexity**: **O(N)+O(N)** (worst is it will pop will elements)
