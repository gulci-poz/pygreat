# krotki

# dowolne typy, zagnieżdżanie, operacje na sekwencjach

t = (1, 2, 3, 4)
print(len(t))
# krotkę definiuje przecinek, w tym przypadku potrzebne są również nawiasy
print(t + ('hello',))
print(t[-1])
print(t.index(1))
# zawsze będzie 1 lub zero, ponieważ krotka nie zapisuje duplikatów
print(t.count(1))

# zmiana tylko przez podstawienie nowego obiektu
t = (0,) + t[:]
print(t)

# przy definicji możemy pominąć nawiasy
t = 'spam', 34, [2013, 2015]
print(t)
# możemy uzupełnić zmienialną strukturę znajdującą się w krotce
t[-1].append(1984)
print(t)

# mamy też typ named tuples
