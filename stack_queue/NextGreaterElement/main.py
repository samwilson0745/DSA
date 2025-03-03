def next_greater_element(arr) -> list[int]:
    nge = [-1] * len(arr)
    stack = []
    for i in range(len(arr)-1,-1,-1):
        while not len(stack)==0 and stack[-1]<=arr[i]:
            stack.pop()
        if len(stack)==0:
            nge[i] = -1
        else: 
            nge[i] = stack[-1]
        stack.append(arr[i])
    return nge


arr = next_greater_element([6,0,8,1,3])
print(arr)