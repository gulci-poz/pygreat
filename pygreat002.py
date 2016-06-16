import math
import random

# ctrl + shift + num pad +

# Review typów

# Numbers

# dostępne są liczby rzeczywiste, z numeratorem i denominatorem
# liczby zespolone
# decimals - ze zminną precyzją

# samo obliczenie zajmuje dłuższą chwilę, nie ma co drukować
# print(len(str(2 ** 1000000)))

# drukowanie w postaci str
print(3.1415 * 2)

# w postaci repr (as-code), bez różnicy - podobnie w konsoli
# w starszym pythonie repr drukuje z większą precyzją
print(repr(3.1415 * 2))

print(math.pi)
print(math.sqrt(math.pi))

print(math.floor(random.random() * 100))
print(random.choice([1, 2, 3, 4]))

# String

# przechowuje zawartość tekstową
# lub kolekcję bajtów (np. załadowany plik graficzny)
# sekwencja - pozycyjnie uporządkowana kolekcja obiektów
# stringi są sekwencjami jednoznakowych stringów
# listy i krotki są również sekwencjami

# operacje na sekwencjach

s = 'spam'
print('spam length:', len(s))

# indeksy to offsety od zerowego elementu
print(s[2])
# ostatni indeks jest -1
# formalnie, ostatni indeks jest dodawany do len()
print(s[-1])

# zmienna jest tworzona w momencie przypisania wartości
# możemy jej przypisać dowolny obiekt
# kiedy pojawia się w wyrażeniu jest zastępowana swoją wartością
# przed użyciem musi mieć przypisaną wartość

# wszędzie, gdzie python spodziewa się wartości możemy użyć literały,
# zmiennej lub dowolnego wyrażenia
print(s[1 + 2])

# slice, zbiór [)
# slice zwraca nowy obiekt, nie zmienia zmiennej, z której wykrawa
print(s[1:3])

# nowy obiekt liczby kopiuje wartość, nie zapisuje referencji
k = 1
l = k
l += 2
print(k)
print(l)

# slice domyślnie jest [0, len()) czyli łącznie z len() - 1
# możemy omijać początkowy lub końcowy indeks
# możemy zrobić klon
print(s[:])

# możemy używać negatywnych indeksów
print(s[:-1])

# + i * działa na sekwencjach; polimorfizm operatorów, zależy od obiektów
# (przeładowanie operatorów)
print(s + 'abc')
print(s * 2)

# stringi są niezmienialne (immutable), możemy przypisać do zmiennej nowy
# obekt string, ale nie możemy zmienić wartośći na danej pozycji
# po przypisaniu nowego obiektu GC robi porządek ze star
s = 'z' + s[1:]
print(s)

# każdy obiekt w pythonie jest immutable lub nie
# liczby, stringi i krotki są immutable
# listy, słowniki i zbiory można zmieniać in place
# większość obiektów tworzonych z class będzie również zmienialnych

# można zmienić string przez przypisanie pojedynczych znaków do listy i
# powrotnej konwersji do stringa
s = 'shrubbery'
l = list(s)
print(l)
l[1] = 'c'
s = ''.join(l)
print(s)

# jest również typ bytearray, hybryda niezmienialnych bajtowych stringów
# oraz zmienialnych list
# w pythonie 3 konieczne jest dodanie b
b = bytearray(b'spam')
b.extend(b'eggs')
print(b)
# mamy zmiany w miejscu, ale tylko dla znaków 8-bitowych (ASCII)
b[0] = ord('k')
print(b)
print(b.decode())

# wbudowane funkcje lub wyrażenia mogą działać na wielu typach (np. sekwencje)
# operacje dla danego typu obiektu są dostępne jako metody

# metody dla stringów

# find() zwraca offset substringa lub -1, gdy substring nie występuje
s = 'spam'
print(s.find('pa'))
s.replace('pa', 'xyz')
# nie zmieniamy stringa, replace() zwraca nowy obiekt
print(s)

# sorted działa dla sekwencji, posortowane elementy stringa zwraca jako listę
# nie zmienia stringa
print(sorted(s))

# sort() działa na liście, zmiany są dokonywane w obiekcie
# sorted zwraca nowy obiekt, działa dla sekwencji
l = ['z', 'y', 'x']
print(sorted(l))
print(l)
l.sort()
print(l)

line = 'aaaa,bbbb,cccc,dddd'
print(line.split(','))
s = 'spam'
print(s.upper(), s.lower())
print(s.isalpha(), s.isdigit())

line = 'aaaa,bbbb,cccc,dddd\n'
print(line.rstrip())
# ewalucja jest od lewej do prawej, z pośrednim tymczasowym wynikiem
print(line.rstrip().split(','))

# wyrażenie formatujące
print('%s, eggs, and %s' % ('spam', 'SPAM!'))

# metoda formatująca (py 2.6, 3.0)
# można kilka razy użyć tego samego numeru
print('{0}, eggs, and {1}'.format('spam', 'SPAM!'))

# można pominąć numery argumentów, są one podstawiane w kolejności (py 2.7, 3.1)
print('{}, eggs, and {}'.format('spam', 'SPAM!'))

# dwukropek oznacza podanie specyfikacji formatowania, dalej dajemy opcje
# formatowania
print('{:,.2f}'.format(296999.2567))

# + oznacza wypisanie znaku liczby
print('%.2f | %+05d' % (3.14159, -42))

# wylicza zmienne w zasięgu wywołującego
# print(dir())

# wylicza atrybuty obiektu (tutaj mamy String)
# print(dir(''))

s = 'spam'
# metoda do celów implementacyjnych (~prywatna)
s = s.__add__('abc')
print(s)

# funkcja help(), możemy szukać wybranego atrybutu
# print(help(s.replace))

# dla przeszukania całej klasy nie wystarczy podać zmiennej danego typu
# jeśli damy samo s, to dostaniemy radę, co powinniśmy podać
# dla Stringa podajemy str
# print(help(str))

# sekwencje escape
# python drukuje znaki możliwe do wydrukowania lub notację heksadecymalną
# \n i \t są liczone jako jeden znak każde
s = 'A\nB\tC'
print(len(s))
# kod ASCII
print(ord('\n'))
# zerowy bajt, nie kończy stringa, \x00 w heks - nie idzie wyświetlić
# w konsoli wyświetla \x00, w pyCharm nieznany znak - prostokąt
# z repr() dostaniemy \x00
s = 'A\0B\0C'
print(len(s))
print(s)
print(repr(s))

# linie są konkatenowane ze znakami końca linii
# pyCharm wyświetla z formatowaniem nowej linii, chyba że damy repr()
# konkatenacja dotyczy również innych sekwencji escape, np. ' i "
msg = """
"aaaa"
'bbbb'
cccc
dddd
"""

print(msg)
print(repr(msg))

# pyCharm domyślnie używa str zamiast repr

# nie trzeba eskejpować ' i "
s = "he'llo"
print(s)
s = 'he"llo'
print(s)

# raw string literal, umożliwia zapisywanie surowych stringów
# bez eskejpowania za pomocą \
s = r'C:\python\bin'
print(s)

# py3
# str obsługuje Unicode (uwzględnia znaki ASCII)
# type bytes reprezentuje surowe wartości byte
# stringi unicode py2.X są traktowane tak samo jak normalne str w py3
print('sp\xc4m')
print(b'sp\xc4m')
print(u'sp\u00c4m')

# w py2.X normal str reprezentuje znaki ASCII i surowe bajty
# inny typ unicode reprezentuje znaki Unicode (przedrostek u)
# literały bajtowe z py3 mają wsparcie od py2.6
# są one traktowane tak samo jak normal str w py2.X

# formalnie w obu pythonach stringi nie-Unicode to sekwencje 8-bitowych bajtów
# stringi Unicode to sekwencje code points Unicode (to nie są bajty)
# niektóre code points są zbyt duże do zakodowania w 1 bajcie w określonym
# kodowaniu, np. utf16

# zakodowane na 4 bajtach
print('spam'.encode('utf8'))
# zakodowane na 10 bajtach
print('spam'.encode('utf16'))

# znaki nie-ASCII można kodować za pomocą \x \u (short) i \U (long)
# stringi bajtowe używają tylko notacji heks \x
# można także zadeklarować kodowanie dla całego pliku
print('sp\xc4\u00c4\U000000c4m')

# zakodowane bajty i code points są takie same dla wybranego kodowania i znaków
print('\u00A3', '\u00A3'.encode('latin1'), b'\xA3'.decode('latin1'))

# py2.X pozwala na mieszanie w wyrażeniu stringów Unicode i normalnych
# (te muszą być ASCII, nie bytes)
# w py3.X konieczna jest konwersja explicite

# tylko py2.X
# print(u'x' + b'y')

# działa również w py3.X
print(u'x' + 'y')

# z konwersjami, dla drukowania jako u (znak ignorowany) lub b
print('x' + b'y'.decode())
print('x'.encode() + b'y')

# przetwarzanie Unicode przeważnie ogranicza się do transferowania danych
# tekstowych z i do pliku
# w pliku tekst jest w zapisany w bajtach, w pamięci jest dekodowany
# do znaków (code points)
# załadowany do stringa tekst przetwarzamy w zdekodowanej formie

# pliki w py3.X są content-spcific
# pliki tekstowe akceptują nazwane kodowania, akceptują i zwracają stringi str
# pliki binarne zapisują stringi bytes
# w py2.X zapisują bajty str; moduł codecs używa typu unicode
