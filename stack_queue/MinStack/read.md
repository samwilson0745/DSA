# MinStack Design

## Problem Statement
Design a stack that supports the following operations in **O(1) time complexity**:

- `push(int val)`: Pushes the element `val` onto the stack.
- `pop()`: Removes the element on the top of the stack.
- `top()`: Retrieves the top element of the stack.
- `get_min()`: Retrieves the minimum element in the stack.

## Solution 1: Using a Pair (Value, Minimum)

### Approach
This approach ensures O(1) time complexity by storing a **pair** inside the stack:

1. Declare an empty list as the stack.
2. Each `push` operation stores:
   - The value itself.
   - The minimum value seen so far.
3. `pop`, `top`, and `get_min` operations retrieve values in O(1) time.
4. Since a pair is immutable, we use a class instead of tuples.

### Implementation
```python
class Pair:
    def __init__(self, val, min_val):
        self.first = val
        self.second = min_val

class Stack:
    def __init__(self):
        self.stack = []
    
    def _is_empty(self):
        return len(self.stack) == 0
    
    def push(self, val):
        print(f"Pushing value: {val}")
        if self._is_empty():
            self.stack.append(Pair(val, val))
        else:
            top = self.stack[-1]
            min_val = min(top.second, val)
            self.stack.append(Pair(val, min_val))
    
    def pop(self):
        if self._is_empty():
            print("Empty Stack")
            return
        print(f"Popping element {self.stack[-1].first}")
        self.stack.pop()
    
    def top(self):
        if self._is_empty():
            print("Empty Stack")
            return -1
        return self.stack[-1].first
    
    def get_min(self):
        if self._is_empty():
            print("Empty Stack")
            return -1
        return self.stack[-1].second

if __name__ == "__main__":
    stack = Stack()
    stack.push(5)
    stack.push(4)
    print(f"Top value: {stack.top()}")
    print(f"Min value: {stack.get_min()}")
    stack.pop()
    stack.push(2)
    stack.push(3)
    print(f"Top value: {stack.top()}")
    print(f"Min value: {stack.get_min()}")
```

### Complexity Analysis
- **Time Complexity**: O(1) for all operations.
- **Space Complexity**: **O(2N)** (each element stores an additional min value).

---

## Solution 2: Optimized Space Complexity

### Approach
To reduce space complexity from **O(2N) to O(N)**, we:
1. Store only the values in the stack.
2. Maintain a separate `min_val` variable.
3. If a pushed value is smaller than `min_val`, store `2 * val - min_val` instead of `val`.
4. When popping, restore the previous `min_val` using the stored formula.

### Implementation
```python
class Stack:
    def __init__(self):
        self.stack = []
        self.min_val = -1
    
    def _is_empty(self):
        return len(self.stack) == 0
    
    def push(self, val):
        print(f"Pushing {val}")
        if self._is_empty():
            self.min_val = val
            self.stack.append(val)
        else:
            if val >= self.min_val:
                self.stack.append(val)
            else:
                self.stack.append(2 * val - self.min_val)
                self.min_val = val
    
    def pop(self):
        if self._is_empty():
            return
        print(f"Popping {self.stack[-1]}")
        m = self.stack.pop()
        if m < self.min_val:
            self.min_val = 2 * self.min_val - m
    
    def top(self):
        if self._is_empty():
            return -1
        m = self.stack[-1]
        return self.min_val if m < self.min_val else m
    
    def get_min(self):
        if self._is_empty():
            return -1
        return self.min_val
```

### Complexity Analysis
- **Time Complexity**: O(1) for all operations.
- **Space Complexity**: **O(N)** (only storing values, no extra pairs).

---

## Conclusion
| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| **Solution 1 (Pair Approach)** | O(1) | O(2N) | Uses extra space to store min values with elements. |
| **Solution 2 (Optimized)** | O(1) | O(N) | Uses formula-based min tracking, reducing space usage. |

- **Use Solution 1** when memory is not a concern and you prefer readability.
- **Use Solution 2** for a more space-efficient solution.