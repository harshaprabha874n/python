#maximum Element
arr=[10,20,40,60]
max=arr[0]
for i in range(1,len(arr)):
	if(arr[i]>max):
	 max=arr[i]
print(max)

#take input
arr=list(map(int,input("Enter the element seperated by comma").split(",")))
print("Array:",arr)
max=arr[0]
for i in range(1,len(arr)):
	if arr[i]>max:
		max=arr[i]
print(max)
