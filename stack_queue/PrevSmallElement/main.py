def prev_smaller_element(arr):
    pse = [-1]*len(arr)
    stack = []
    for i in range(0,len(arr)):
        while len(stack)!=0 and stack[-1] >= arr[i]:
            stack.pop()
        
        pse[i] = -1 if len(stack)==0 else stack[-1]
        stack.append(arr[i])
    return pse

print(prev_smaller_element([4,5,2,10,8]))