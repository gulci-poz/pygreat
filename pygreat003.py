import re

# pattern matching

# w nawiasach [] dajemy zestaw znaków
# nawiasy oznaczają, że znaleziony napis (zgodny ze wzorcem) zostanie
# zapisany jako grupa dopasowania
match = re.match('Hello[ \t]*(.*)world', 'Hello, Python 3.X world')
print(match.group(1))

# similar to splitting by an alternatives pattern
# podaliśmy wzorzec trzy razy, więc otrzymamy trzy grupy
match = re.match('[/:](.*)[/:](.*)[/:](.*)', '/usr/home:lumberjack')
print(match.groups())

# pusty string przed pierwszym ukośnikiem
print(re.split('[/:]', '/usr/home/lumberjack'))
