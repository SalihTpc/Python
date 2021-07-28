def asal_mi(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
            return True


while True:
    sayi = input("Number:")
    if sayi == "q":
        print("Program is shooting down...")
        break
    else:
        sayi = int(sayi)
        if asal_mi(sayi):
            print(sayi, "is a prime number.")
        else:
            print(sayi, "is not a prime number.")
