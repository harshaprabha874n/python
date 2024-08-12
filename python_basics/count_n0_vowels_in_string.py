#count the no of vowels in a string
string="Harsha Prabha"
count=0
for i in string:
    if i =="a"or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
        i=string
        count+=1
print(count)

#take input
string=input("enter the string")
count=0
vowels="aeiouAEIOU"
for i in string:
    if i in vowels:
        count+=1
print(count)

