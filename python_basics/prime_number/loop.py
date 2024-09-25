num=int(input("Enter the number:"))
sump=0
for i in range(2,num):
    if(num%i==0):
        sump=sump+i
        if(sump==num):
          print("Prime")
          break
        else:
           print("Not")