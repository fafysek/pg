def je_prvocislo(cislo):
    if cislo < 2:
        return False

    for i in range(2, cislo):
        if cislo % i == 0:
            return False

    return True



def vrat_prvocisla(maximum):
    seznam_prvocisel = [] #prázdný seznam

    for n in range(2, maximum + 1):
        if je_prvocislo(n):
            seznam_prvocisel.append(n)

    return seznam_prvocisel

if __name__ == "__main__":
    cislo = int(input("Zadej číslo: "))

    if je_prvocislo(cislo):
        print(f"Číslo {cislo} je prvočíslo")
    else:
        print(f"Číslo {cislo} není prvočíslo")


    max = int(input("Zadej maximum: "))
    prvocisla = vrat_prvocisla(max)
    print(prvocisla)