# słowniki

# słowniki są mapowaniami
# indeksowanie jest po kluczach, nie ma porządku pozycyjnego
# jedyne mapowanie w core python, które jest mutable

# pyCharm narzeka, że możemy użyć literału
# d = {'food': 'spam', 'quantity': 4, 'color': 'pink'}
# d = dict({'food': 'spam', 'quantity': 4, 'color': 'pink'})

# można też przypisywać nowe klucze/wartości
# d = {}
# d['food'] = 'spam'

# składnia name=value
d = dict(food='spam', quantity=4, color='pink')

d['food'] = 'salad'
d['quantity'] += 1
print(d)

# zipowanie
bob = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40]))
print(bob)

# zagnieżdżanie
rec = {'name': {'first': 'Bob', 'last': 'Smith'},
       'jobs': ['dev', 'mgr'],
       'age': 40.5}
print(rec)
print(rec['name']['last'])
print(rec['jobs'][0])

# dodanie nowych wartości do listy i słownika
# w liście nie możemy wyskoczyć poza indeks, zarówno przy przypisaniu,
# jak i przy odczycie
# kiedy tracimy ostatnią referencję do obiektu, jest on usuwany z pamięci
# przec py GC, np. przypisanie do zmiennej nowej wartości
# możemy dowolnie rozszerzać zagnieżdżone struktury
rec['jobs'].append('janitor')
rec['name']['mother'] = 'Kowalski'
print(rec)

# object persistance system, możemy przechowtwać natywne obiekty pythona
# w plikach lub bazach danych access-by-key, obiekty są automatycznie
# tłumaczone na strumienie bajtów (moduły persistence pickle i shelve)
# mamy moduł json do translacji JSON do obiektów pythona
# PyMongo; MongoDB - language-neutral binary-encoded
# serialization of JSON-like documents

numdict = {'a': 1, 'b': 2, 'c': 3}
# możemy przypisać coś do nowego, nieistniejącego klucza
# nie możemy odwoływać się do nieistniejącego klucza
# print(numdict['d'])
print('f' in numdict)
# korzystamy z not in, a nie not 'f' in (działa, ale PEP8 wskazuje inaczej)
if 'f' not in numdict:
    print('missing')

# inne metody sprawdzania istnienia
# get() zwraca podaną domyślną wartość
print(numdict.get('x', 0))

# w py2.X była metoda has_key(), nie ma jej w py3.X

# "ternary if/else"
print(numdict['x'] if 'x' in numdict else 0)

# z try możemy obsłużyć wyjątek

# porządkowanie kluczy
nk = list(numdict.keys())
nk.sort()
for key in nk:
    print(key, '=>', numdict[key])

print(sorted(numdict))
# w tym przypadku sorted() sortuje automatycznie klucze słownika
# i zwraca je w postaci listy
# słownik nie jest sekwencją, ale jest iterable; next daje kolejne klucze
# for jest operacją na obiektach iterable
for key in sorted(numdict):
    print(key, '=>', numdict[key])

x = 4
while x > 0:
    print('spam!' * x)
    x -= 1

# kiedy obiekt jest iterable
# - fizycznie przechowywana w pamięci sekwencja
# - obiekt generuje jedną jednostkę (item) w czasie w kontekście operacji
# iteracji (~ wirtualna sekwencja)
# takie obiekty wspierają protokół iteracji pythona - odpowiadają na
# wywołanie iter obiektem, który pojawia sią w odpowiedzi na wywołanie next
# wyjątek jest wyrzucony po zakończeniu produkowania wartości
# przykładami są generator i obiekt pliku, który iteruje linia po linii
# range i map działa dla obiektów iterable, od py3.X
# każde narzędzie, które skanuje obiekt od lewej do prawej korzysta
# z protokołu iteracji
# comprehension możemy zawsze zakodować jako pętlę for
# wewnętrznie oba te rozwiązania korzystają z protokołu iteracji
# w szczególnych przypadkach comprehension i narzędzie programowania
# funkcyjnego (map, filter) działają szybciej niż for (big data)

# simplicity, readability first, potem performance; optymalizacje w pythonie
# pojawiają się z wersji na wersję
# moduły time, timeit, profile

