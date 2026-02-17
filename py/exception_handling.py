#ERROR Handling :
while True:
    try:
        n1 = int(input("First num : "))
        n2 = int(input("Second num : "))
        n3 = n1/n2
        print(f"{n1}/{n2} = {n3}")
        break
    except ValueError: #for input of strings
        print("*input num must be Interger")
    except ZeroDivisionError: # stopping zero from dividing
        print("*cannot divide number with zero")
