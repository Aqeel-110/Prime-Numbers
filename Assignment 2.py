while True:
    a = int(input("Enter First Number : "))
    b = int(input("Enter Second Number : "))

    if a < b:
        print("The Prime Numbers in the range are: ")
        for num in range(a, b + 1):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    print(num)
    else:
        print("Wrong Range")

    c = input("Enter '*' to Stop or Press any Key to Continue : ")
    if c == "*":
        break
    else:
        continue
