# Part I - python database usage - 12

# hierarchia koncepcyjna
# 1 programy są zbudowane z modułów
# 2 moduły zawierają stwierdzenia (statements)
# 3 stwierdzenia zawierają wyrażenia (expressions)
# 4 wyrażenia tworzą i przetwarzają obiekty

# filary programowania
# sekwencja: zrób najpierw to, potem tamto
# selekcja: zrób to, jeśli coś jest prawdziwe
# powtórzenie: zrób to wiele razy

# w pythonie wiele wyrażeń zawiera się równocześnie w kilku kategoriach
# ważniejszą zasadą porządkującą język są w pythonie obiekty

# w pythonie wszystko jest obiektem
# wszystko, co przetwarzamy jest rodzajem obiektu
# obiekt to struktura danych
# obiekt definiuje dane i operacje na nich
# operacje są powiązane z obiektami danego typu
# możemy wykonać tylko operacje, które są uprawnione dla danego typu obiektu
# mamy silne typowanie
# składnia determinuje typ obiektu, który definiujemy
# mamy dynamiczne typowanie

# wbudowane typy obiektów (core data types)
# literał to wyrażenie, którego składnia generuje obiekt
# literał bywa nazywany stałą
# obiekty są również generowane przez stwierdzenia
# (np. def, class, import, lambda)
# oraz przez inne obiekty (np. funkcje; funkcja to obiekt)

# Numbers
# 1234
# 3.14
# 3 + 4j
# 0b111
# Decimal()
# Fraction()

# Strings
# 'spam'
# "Bob's"
# py2
# b'a\x01c'
# u'sp\xc4m'

# Lists
# [1, [2, 'three'], 4.5]
# list(range(10))

# Dictionaries
# {'food': 'spam', 'taste': 'yum'}
# dict(hours=10)

# Tuples
# (1, 'spam', 4, 'U')
# tuple('spam')
# namedtuple

# Files
# open('eggs.txt')
# open(r'C:\ham.bin', 'wb')

# Sets
# set('abc')
# {'a', 'b', 'c'}

# Other core types
# Booleans
# types
# None

# Program unit types
# funkcje
# moduły
# klasy

# Implementation-related types
# compiled code (dla budujących narzędzia)
# stack tracebacks

# mamy jeszcze typy zdefiniowane w modułach biblioteki standardowej

# Numbers - 97
