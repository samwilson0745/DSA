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
            if val > self.min_val:
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
        return self.min_val

def main():
    stack = Stack()
    print("Stack initialised")
    print("Pushing 3, 5")
    stack.push(3)
    stack.push(5)
    print(f"Top of stack: {stack.top()}")
    print(f"Minimum of stack: {stack.get_min()}")
    print("Pushing 2")
    stack.push(2)
    print(f"Top of stack: {stack.top()}")
    print(f"Minimum of stack: {stack.get_min()}")
    print("Popping")
    stack.pop()
    print(f"Top of stack: {stack.top()}")
    print(f"Minimum of stack: {stack.get_min()}")
    print("Pushing 1")
    stack.push(1)
    print(f"Top of stack: {stack.top()}")
    print(f"Minimum of stack: {stack.get_min()}")

if __name__ == "__main__":
    main()

# class Pair:
#     def __init__(self, val, min_val):
#         self.first = val
#         self.second = min_val

# class Stack:
#     def __init__(self):
#         self.stack = []
    
#     def _is_empty(self):
#         return len(self.stack) == 0
    
#     def push(self, val):
#         print(f"Pushing value: {val}")
#         if self._is_empty():
#             self.stack.append(Pair(val, val))
#         else:
#             top = self.stack[-1]
#             min_val = min(top.second, val)
#             self.stack.append(Pair(val, min_val))
    
#     def pop(self):
#         if self._is_empty():
#             print("Empty Stack")
#             return
#         print(f"Popping element {self.stack[-1].second}")
#         self.stack.pop()
    
#     def top(self):
#         if self._is_empty():
#             print("Empty Stack")
#             return -1
#         return self.stack[-1].first
    
#     def get_min(self):
#         if self._is_empty():
#             print("Empty Stack")
#             return -1
#         return self.stack[-1].second

# if __name__ == "__main__":
    stack = Stack()
    stack.push(5)
    stack.push(4)
    print(f"Top value: {stack.top()}")
    print(f"Min value: {stack.get_min()}")
    stack.pop()
    stack.push(2)
    stack.push(3)
    print(f"Top values: {stack.top()}")
    print(f"Min value: {stack.get_min()}")