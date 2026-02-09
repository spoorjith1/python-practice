while True:
    try:
        n1 = int(input("First num : "))
        n2 = int(input("Second num : "))
        n3 = n1/n2
        print(n3)
        break
    except ValueError:
        print("*input num must be Interger")
    except ZeroDivisionError:
        print("*cannot divide number with zero")
