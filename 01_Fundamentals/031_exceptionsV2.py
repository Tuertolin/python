print("Insert 2 numbers to be diveded")
print("Enter 'q' to exit")

while True:
    first_number = input("\nFirstr number:")
    if first_number == 'q':
        break
    
    second_number = input("\nSecond  number:")
    if first_number == 'q':
        break
    
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)