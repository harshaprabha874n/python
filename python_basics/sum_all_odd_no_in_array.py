arr=[10,33,21,0,9,8]
sum=0
for i in arr:
    if i%2==0:
        even=i
    else:
        sum=sum+i
print(sum)

#take input
arr=list(map(int,input("enter the array separated by comma").split(",")))
sum=0
for i in arr:
    if i%2==0:
        even=i
    else:
        sum=sum+i
print(sum)