# unicode text files

s = 'sp\xc4m'
print(s)

# jeśli formatowanie dla naszej platformy różni się od tego,
# w którym chcemy odczytywać/zapisywać
file = open('unidata.txt', 'w', encoding='utf-8')
print(file.write(s))
file.close()

# automatyczne zamknięcie pliku
text = open('unidata.txt', encoding='utf-8').read()
print(text)
print(len(text))

# w trybie binarnym
raw = open('unidata.txt', 'rb').read()
print(raw)
# 5 surowych bajtów w unicode, znaków jest 4
print(len(raw))

# można kodować/dekodować ręcznie (np. email, połączenie sieciowe zamiast pliku)
print(text.encode('utf-8'))
print(raw.decode('utf-8'))

print(text.encode('latin-1'))
print(text.encode('utf-16'))

print((len(text.encode('latin-1')), len(text.encode('utf-16'))))
print(b'\xff\xfes\x00p\x00\xc4\x00m\x00'.decode('utf-16'))

# w py2.X stringi Unicode pokazuje z u
# w py2.X pliki tekstowe Unicode muszą być otwierane za pomocą codecs.open

# nazwy plików mogą być non-ASCII
# narzędzia walkers i listers - więcej kontroli

# inne narzędzia file-like: pipes, FIFOs, sockets (wspierają networking oraz
# interprocess communication), keyed-access files,
# persistent object shelves, descriptor-based files (wspierają file locking),
# relational and object-oriented database interfaces, +++
