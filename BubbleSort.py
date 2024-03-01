def Bubble_sort(arr,n):
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]       
    print(arr)

def selection_sort(arr,n):
    
    print(arr)


n=int(input("Enter the size of the array: "))
print("Enter the elements in the array: ")
arr=[int (x) for x in input().split()]
Bubble_sort(arr,n)