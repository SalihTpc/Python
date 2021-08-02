def prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


print("""
**********************************************************

Let's Find prime number of list up to given number by you.
 
Press 'q' for quit...

**********************************************************
 """)

while True:
    e = input("Number:")
    if e == "q":
        print("Program is shooting down...")
        break
    else:
        try:
            liste = list()
            e = int(e)
            for j in range(2, e + 1):
                if prime(j):
                    liste.append(j)
            print(liste)
        except ValueError:
            print("Wrong entry\nPlease enter correct one...")
