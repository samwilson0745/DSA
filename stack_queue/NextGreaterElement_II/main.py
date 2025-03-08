def next_greater_element(arr)->list[int]:
    n = len(arr)
    if(n==1):
        return [-1]
    nge = [-1]*n    
    stack = []
    for i in range(2*n-1,-1,-1):
        while not len(stack)==0 and stack[-1]<=arr[i%n]:
            stack.pop()
        if i<n:
           nge[i] = -1 if len(stack)==0 else stack[-1]
        stack.append(arr[i%n])
    return nge

result = next_greater_element([1,2,3,4,5])
print(result)