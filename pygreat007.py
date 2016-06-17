# pliki

# nadpisanie całego pliku
f = open('data.txt', 'w')
# w py3.X zwraca ilość zapisanych znaków
f.write('hello\n')
print(f.write('world\n'))
f.close()

# zawartość pliku to zawsze string
# domyślnie jest 'r'
f = open('data.txt')
text = f.read()
print(text)
print(text.split())
f.close()

# możemy opcjonalnie podać maksymalny rozmiar znaku
# metoda readline
# metoda seek

# najlepiej nie odczytywać pliku, mamy iterator korzystający z for
# automatyczne zamknięcie pliku
for line in open('data.txt'):
    print(line)
