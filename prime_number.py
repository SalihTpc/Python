def prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True
    return False


while True:
    sayi = input("Number:")
    if sayi == "q":
        print("Program is shooting down...")
        break
    else:
        try:
            sayi = int(sayi)
            if prime(sayi):
                print(sayi, "is a prime number.")
            else:
                print(sayi, "is not a prime number.")
        except ValueError:
            print("Wrong entry\nPlease enter correct one...")