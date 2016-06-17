# listy

l = [123, 'spam', '1.23']
print(len(l))
print(l[0])
print(l[:-1])
print(l[:len(l)])
# ;)
print(len(l[:len(l)]))
# + i * zwracają nowe listy
lcon = l + [4, 5, 6]
print(lcon)
lrep = l * 2
print(lrep)
print(l)

# metoda rozszerza listę o bajty stringa jako odrębne elementy listy
l.extend('hello')
print(l)

l = list([123, 'spam', '1.23'])
# pyCharm narzeka, że możemy użyć literału (przy powtórnym przypisaniu)
# l = [123, 'spam', '1.23']
l.append('hello')
print(l)

# pop() zwraca element i usuwa go z listy
k = l.pop(2)
print(k)
print(l)
# do samego usuwania możemy użyć del (statement)
del l[-1]
print(l)

l.insert(1, 'world')
print(l)
l.remove('spam')
print(l)

m = ['bb', 'aa', 'cc']
# to są operacje w miejscu, nie mamy zwróconego obiektu, więc nie możemy
# zrobić chainingu
m.sort()
m.reverse()
print(m)

# tutaj pyCharm nie narzeka
m = ['bb', 'aa', 'cc']
m.sort(reverse=True)
print(m)

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(m)
print(m[1])
print(m[1][1])

# list comprehension expression

# wyrażenie jest wykonywane dla każdego elementu w sekwencji
# wyrażeniem jest row[1], mamy sekwencję list z m (lista list)
# również dla kilku typów, które nie są sekwencjami
col2 = [row[1] for row in m]
print(col2)
col2plus = [row[1] + 1 for row in m]
print(col2plus)
col2mod = [row[1] for row in m if row[1] % 2 == 0]
print(col2mod)
col2bin = [(row[1] % 2 == 0) for row in m]
print(col2bin)

# możemy iterować po dowolnym obiekcie iterable
diag = [m[i][i] for i in [0, 1, 2]]
print(diag)

doubles = [c * 2 for c in 'spam']
print(doubles)
print(''.join(doubles))
doubles = [c.upper() + c for c in 'spam']
print(doubles)
print(''.join(doubles))
codes = [ord(c) for c in 'spam']
print(codes)
# print('\x73')

# w py3 wymagane jest otoczenie list()
print(list(range(4)))
# od, do, co ile
print(list(range(-6, 7, 2)))

# w comprehension możemy zebrać wiele wartości,
# musimy je opakować w zagnieżdżoną kolekcję
# dostaniemy listę list
compr1 = [[x ** 2, x ** 3] for x in range(4)]
print(compr1)
compr2 = [[x, x / 2, x * 2] for x in range(-7, 6, 2) if x > 0]
print(compr2)
compr3 = [2 ** i for i in range(21)]
print(compr3)

# składnia comprehension została zgeneralizowana
# można wyprodukować nie tylko listę
# ujmując comprehension w nawiasy możemy utworzyć generator,
# który produkuje rezultaty na żądanie
g = (sum(row) for row in m)
print(next(g))
print(next(g))
print(next(g))
# obiekt generatora
print(g)
# następne wywołanie dałoby błąd

# rezultaty przepuszczenia elementów przez funkcję
# w py3 trzeba użyć list(), w py2 od razu dostajemy listę
mapsum = list(map(sum, m))
print(mapsum)

# w py2.7 i py3.X można użyć składni comprehension do utworzenia set i dict
setsum = {sum(row) for row in m}
print(setsum)
dictsum = {i: sum(m[i]) for i in range(3)}
print(dictsum)

print("Podsumowanie comprehensions")
# lista
print([ord(x) for x in 'spaam'])
# zbiór, usuwamy duplikaty
print({ord(x) for x in 'spaam'})
# słownik, klucze muszą być unikalne
# w tym przypadku będzie naspisywana ta sama wartość, ale nie musi tak być
print({x: ord(x) for x in 'spaaaaam'})
dictlist = [1, 1, 1, 2, 2, 3, 6, 6, 9, 9]
# tutaj jest ok, bo kluczujemy po unikalnych wartościach
print({i: dictlist[i] for i in range(len(dictlist))})
# tutaj kluczujemy po wartościach z listy,
# które nie są unikalne i dostaniemy tylko ostatnią nadpisaną wartość
print({dictlist[i]: i for i in range(len(dictlist))})
