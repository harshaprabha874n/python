arr=[10,20,30,80,30,30,30]
element=30
count=0
for i in arr:
    if i==element:
        count+=1
print(count)

#take input
arr=list(map(int,input("Enter the array sepearated by comma:").split(",")))
checkelement=int(input("Element to check:"))
count=0
for i in arr:
    if i==checkelement:
        count+=1
print(count)
