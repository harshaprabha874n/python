def fibo(n):
    n1,n2=0,1
    for i in range(0,n):
        n3=n1+n2
        n1=n2
        n2=n3
        print(n2,end="")
n=int(input("Enter the number:"))
fibo(n)