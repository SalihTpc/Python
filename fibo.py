a = 1
b = 1
fibo = [a, b]
c = int(input("When do you want stop fibonacci list\nPlease give me a number:"))
while True:
    a, b = b, a + b
    fibo.append(b)
    if b >= c:
        break
print(fibo)
