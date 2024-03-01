class Solution:
    def insertAtIndex(self, arr, sizeOfArray, index, element):
        #Your code here
        '''You need to insert the given element at the given index. 
        After inserting the elements at index, elements
        from index onward should be shifted one position ahead
        You may assume that the array already has sizeOfArray - 1
        elements.'''
        temp=0
        for i in range(index,sizeOfArray+1):
            
            if i==index:
                temp=arr[i]
                arr[i]=element
            if i>index and i<sizeOfArray:
                element=arr[i]
                arr[i]=temp
            else:
                arr.append(temp)
        
            
sizeOfArray=int(input())
arr=[int(x) for x in input().strip().split()]
arr.append(-1)
index,element=map(int,input().strip().split())
     
Solution().insertAtIndex(arr,sizeOfArray,index,element)
        
for i in range(sizeOfArray):
    print(arr[i],end=" ")
    print()

