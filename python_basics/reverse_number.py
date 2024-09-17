def reverse_number(number):
    original_number = number
    reverse = 0
 
    for _ in str(number):
        digit = number % 10
        reverse = reverse * 10 + digit
        number //= 10
 
    print(f"Original Number: {original_number}")
    print(f"Reversed Number: {reverse}")
 
reverse = 6789
reverse_number(reverse)