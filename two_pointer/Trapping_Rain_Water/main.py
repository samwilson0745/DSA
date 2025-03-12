def trapping_rain_water(arr):
    lMax=rMax=total=0
    l,r=0,len(arr)-1
    while(l<r):
        if(arr[l]<arr[r]):
            if(lMax>arr[l]):
                total+=lMax - arr[l]
            else:
                lMax = arr[l]
            l=l+1
        else:
            if(rMax>arr[r]):
                total+= rMax - arr[r]
            else:
                rMax = arr[r]
            r=r-1
    return total

print(trapping_rain_water([0,1,0,2,1,0,1,3,2,1,2,1]))
