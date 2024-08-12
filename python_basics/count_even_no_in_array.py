#count the number of even numbers in array
arr=[10,43,55,86]
count=0
for i in arr:
    if i % 2 == 0:
        count+=1
print(count)

# Taking input
arr = list(map(int, input("Enter elements sepaarted by comma: ").split(",")))
print("Array:",arr)
count=0
for i in arr:
    if i%2==0:
        count+=1
print(count)
      
