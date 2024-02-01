loc=-1  #initially we assume target location as -1
def binary_search(list,target):     #takes the list and target as parameters
    low=0   #initially lowerbound will be 0
    high=len(list)-1    #initially the upperbound will be the length of the list
    while low<=high:    
        mid=(low+high)//2       #gets the integer mid index of the list
        if list[mid]==target:   #if the mid value equal to the target then the loc will be the index of the mid
            globals()['loc']=mid
            return True
        else:       #else, checks if the mid value is less than the target then the new lowerbound will be mid+1 index
            if list[mid]<target:
                low=mid+1
            else:   #if the mid value is grater than the target then the new upperbound will be mid-1 index
                high=mid-1
    return False    #at last if the target is not found then the function return false


list=[4,5,6,18,27,34,45,67,75,92]   #sample sorted list(for binary search the list always need to be sorted)
target=45  #example target we need to search in the list
if binary_search(list,target): #calls the binary_search()
    print("The index of Target is: ",loc+1)     #prints the index of the target in the function returns TRUE
else:
    print("Target not found.")  #prints 'target not found' if the funtion returns FALSE