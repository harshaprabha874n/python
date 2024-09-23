def reverse_number(number):
    for i in str(number):
        digit = number % 10
        print(digit,end="")
        number=number//10
 
number= int(input("Enter the Number:"))
reverse_number(number)