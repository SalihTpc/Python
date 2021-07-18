def armstrong(x):
    a = len(x)
    b = list(x)
    total = 0
    for i in b:
        total = total + int(i) ** a
    if total == int(x):
        return f"{x} is an Armstrong number."
    else:
        return f"{x} is not an Armstrong number."


while True:
    number = input("Number:")
    if number == "q":
        print("Program is shutting down...")
        break
    else:
        try:
            print(armstrong(number))
        except ValueError:
            print("It is an invalid entry. Don't use non-numeric, float, or negative values")
