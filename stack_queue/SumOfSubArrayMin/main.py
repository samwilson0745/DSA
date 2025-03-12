def findNSE(arr):
    n = len(arr)
    nse = [-1]*n
    st = []
    for i in range(n-1,-1,-1):
        while len(st)!= 0  and arr[st[-1]]>=arr[i]:
            st.pop()
        nse[i] = n if len(st)==0 else st[-1]
        st.append(i)
    
    return nse
def findPSE(arr):
    n = len(arr)
    pse = [-1]*n
    st = []
    for i in range(0,n):
        while len(st)!=0 and arr[st[-1]]>=arr[i]:
            st.pop()
        pse[i] = -1 if len(st)==0 else st[-1]
        st.append(i)
    return pse

def sum_of_subarray_min(arr):
    nse = findNSE(arr)
    pse = findPSE(arr)
    print(nse,pse)
    total = 0
    for i in range(0,len(arr)):
        left = i - pse[i]
        right = nse[i]-i
        print(total,right,left,arr[i])
        total = total  + (right*left*arr[i])
    return total

print(sum_of_subarray_min([3,1,2,4]))

        
