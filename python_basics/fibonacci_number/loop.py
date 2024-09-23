num=int(input("Enter the number:"))
n1,n2=0,1
for i in range(1,num):
   n3=n1+n2
   n1=n2
   n2=n3

   print (n3,end="")
