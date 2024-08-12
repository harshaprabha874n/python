arr=[10,-2,30,40]
sum=0
for i in range(0,len(arr)):
    if arr[i]>0:
        sum=sum+arr[i]
print(sum)

#take input
arr=list(map(int,input("Enter the array separated by comma").split(",")))
print("Array:",arr)
sum=0
for i in range(0,len(arr)):
    if(arr[i]>0):
        sum=sum+arr[i]
print(sum)