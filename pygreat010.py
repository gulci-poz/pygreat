import decimal
from fractions import Fraction

# other core types

# zbiory - nie są sekwencją ani mapowaniem,
# to nieuporządkowane kolekcje unikalnych obiektów
# zbiory można modyfikować
# py3.X i py2.7

# buduje zbiór z elementów sekwencji
x = set('spam')
y = {'h', 'a', 'm'}
print(x)
print(y)
# krotka złożona z dwóch zbiorów
print((x, y))
y.add('s')
print(y)

# intersekcja
print(x & y)
# unia
print(x | y)
# różnica
print(x - y)
# nadzbiór
print(x > y)

# set comprehension
print({n ** 2 for n in [1, 2, 3, 4]})

# filtrowanie duplikatów
print(list(set([1, 2, 1, 3, 1])))
# wykazanie różnic w kolekcjach
print(set('spam') - set('ham'))
# test równości, z pominięciem porządku
print(set('spam') == set('asmp'))
# testowanie z in (dla wszystkich kolekcji)
print('p' in set('spam'))

# decimals, fixed precision
d = decimal.Decimal('3.141')
print(d)
print(d + 1)

decimal.getcontext().prec = 2
print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))

# liczby rzeczywiste z licznikiem i mianownikiem, fractions
f = Fraction(2, 3)
print(f)
print(f + 1)
print(f + Fraction(1, 2))

# Boolean z obiektami True i False - to integery 1 i 0 ze specjalną logiką
# wyświetlania
print((1 > 2, 1 < 2))
# wartość boolean obiektu
print(bool('spam'))

# obiekt None, do inicjalizacji obiektów i nazw
x = None
print(x)
l = [None] * 10
print(l)

# obiekt type, zwraca go funkcja type()
# wynik różny w py3.X, typy zostały połączone z klasami
print(type(l))
# tutaj widzimy ten typ
print(type(type(l)))

# testowanie typu obiektu
# PEP8 sugeruje użycie isinstance() zamiast porównywania typów
# if type(l) == type([]):
#     print('list ok')

print(isinstance(l, list))

# tutaj nie ma ostrzeżenia
if type(l) == list:
    print('list ok')

# w pythonie nie sprawdzamy typów, tracimy elastyczność i ograniczamy się do
# wybranych typów
# nie jesteśmy "Pythonic"
# kluczem dobrego użycia pythona jest polimorfizm
# kodujemy do interfejsów obiektów (wsparcie operacji), nie typów (klas)
# przejmujemy się co robi obiekt, a nie czym jest
# jeśli obiekt ma kompatybilny interfejs, to kod będzie działał, bez względu
# na typ (polimorfizm)

# len() działa nie tylko na sekwencjach, ale na wszystkich kolekcjach
print(len({'1': 1, '2': 2}))
