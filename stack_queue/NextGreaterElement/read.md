# Next Greater Element

## Problem Statement
What will be the next greater for a given index in an array

## Solution 1: bruteforce approach(Not Optimal)
### Approach
Simple just loop through each element and check the next element

This approach is forward traversing

1. Initialise an empty list 
2. First loop to take each element and second loop to check for each element which is the next greater element
3. Add to the empty list and return

### Complexity Analysis
- **Time Complexity: O(N^2)
- **Space Complexity: O(N)

## Solution 2: Optimal Solution
We are going to use backward traversing and a monotonic stack
Monotonic Stack - elements stored in a specific order (for this case decreasing order)

### Approach
To reduce the time ,we use stack:
1. Initialise an empty stack and an empty list to store the greater values
2. Backward traverse the array 
3. In the loop 
   - Maintain a Monotonic Stack
     - A while loop runs as long as the stack is not empty and the top element of the stack (stack[-1]) is less than or equal to arr[i].
     - If the condition holds, stack.pop() removes the top element since it cannot be the next greater element (NGE) for arr[i].
   - Assign Next Greater Element (NGE)
     - If the stack is empty after popping, it means no greater element exists on the right, so nge[i] = -1.
     - Otherwise, nge[i] = stack[-1], meaning the top of the stack is the next greater element for arr[i].
   - Push The Current Element into the Stack
     - After processing, arr[i] is pushed onto the stack to potentially be the NGE for upcoming elements.
4. Return result

### Complexity Analysis
- **Time Complexity**: **O(2N)** for all operations.
- **Space Complexity**: **O(N)+O(N)** (worst is it will pop will elements)

## Conclusion
- **Use Solution 2** is the optimal here as we are only focusing the time factor

   
