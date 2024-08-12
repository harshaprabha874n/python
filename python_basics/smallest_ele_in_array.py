arr=[10,7,2,1,0,67]
small=arr[0]
for i in range(1,len(arr)):
    if arr[i]<small:
       small=arr[i]
print(small)

#take input
arr=list(map(int,input("enter the array seperated by comma").split()))
print("Array:",arr)
small=arr[0]
for i in range(1,len(arr)):
    if arr[i]<small:
        small=arr[i]
print(small)