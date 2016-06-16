# lists

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

# 110 - Bounds Checking
