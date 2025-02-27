class Stack:
    def __init__(self):
        self.stack = []
        self.min_val = 0
    def push(self,val):
        if(len(self.stack)==0):
            self.min_val = val
            self.stack.append(val)
            return
        else:
            if(val>self.min_val):
                self.stack.append(val)
            else:
                self.stack.append(2*val-self.min_val)
                self.min_val = val
    def pop(self):
        if(len(self.stack)==0):
            return -1
        else: 
            m = self.stack.pop()
            if(m<self.min_val):
                self.min_val = 2*self.min_val-m
    def top(self):
        if(len(self.stack)==0):
            return -1
        else:
            m = self.stack[-1]
            if(m<self.min_val):
                return self.min_val
            else:
                return m
    def get_min(self):
        return self.min_val
    
if __name__ == "__main__":
    stack = Stack()
    print("Stack initialised")
    print("Pushing 3,5")
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