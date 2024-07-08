secret = 5
guess = int(input("Ugotovi število: "))

if guess == secret:
    print("Čestitam, osvojili ste glavno nagrado!")
else:
    print("Ni pravilno.")
    print("***Game over***")
