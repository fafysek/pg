def my_range_while(start, stop, step=1):
    # pomoci cyklu while vytvorte vlastni implementaci funkce range()
    vysledek = []
    x = start
    while (x > stop if step < 0 else x < stop):
        vysledek.append(x)
        x += step
    return vysledek


def my_enumerate_for(iterable, start=0):
    # implementujte funkci enumerate pomoci cyklu for
    vysledek = []
    for x in range(0, len(iterable)):
        vysledek.append((x+start, iterable[x]))
    return vysledek

def my_enumerate_for2(iterable, start=0):
    vysledek = []
    for value in iterable:
        vysledek.append((start, value))
        start += 1
    return vysledek

def my_enumerate_while(iterable, start=0):
    # implementujte funkci enumerate pomoci cyklu while
    vysledek = []
    i = 0
    while i < len(iterable):
        vysledek.append((i + start, iterable[i]))
        i += 1



        
    return vysledek

if __name__ == "__main__":

    #print(list(range(10, 1, -1)))
    #print(my_range_while(10, 1, -1))

    print(list(enumerate(["aaa", "bbb", "ccc"], 100)))
    print(my_enumerate_for(["aaa", "bbb", "ccc"], 100))
    print(my_enumerate_for2(["aaa", "bbb", "ccc"], 100))
    print(my_enumerate_while(["aaa", "bbb", "ccc"], 100))