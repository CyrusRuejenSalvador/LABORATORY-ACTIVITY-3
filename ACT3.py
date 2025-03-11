num = int(input("Choose a Number:"))
if num == 0:
    print("zero")
else:
    if num > 0:
        sign = "Positive"
    else:
        sign = "Negative"
    if num % 2 == 0:
        print(sign, "Even Number")
    else:
        print(sign, "Odd Number")