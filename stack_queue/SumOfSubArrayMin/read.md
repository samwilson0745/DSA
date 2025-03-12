# Sum of SubArray Minimum
## Problem statement 
Of all the possible arrays sum the minimum value out of it

## Solution 1: Bruteforce (Not Optimal)
Iterate through all the possible sub arrays and compare and add
- **Time Complexity**: **O(N^2)** 
- **Space Complexity**: **O(1)** 

## Solution 2: Optimal
1. Find the Next Smaller Element Array and the Previous Smaller element array
2. Iterate through the array and use this formula
  - How many elements can extend to the left while keeping arr[index] as the minimum = index - pse[index]
  - How many elements can extend to the right while keeping arr[index] as the minimum = nse[index]-index
  - now the formula is = total + (left*right*arr[index])
- **Time Complexity**: **O(5N)**
- **Space Complexity**: **O(5N)**
