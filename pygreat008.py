import struct

# binary bytes files

# w py3.X domyślny jest Unicode
# w py2.X mamy bajty (8-bit)
# zawsze są kodowane i odczytywane stringi

# py3.X koduje/dekoduje Unicode, zawartość jest normalnym str
# w przypadku plików binarnych mamy string bajtów
# w py3.X musimy dać explicite b

# pakowanie/odpakowanie surowych bajtów do odczytu/zapisu w pliku binarnym
packed = struct.pack('>i4sh', 7, b'spam', 8)
print(packed)

file = open('data.bin', 'wb')
print(file.write(packed))
file.close()

data = open('data.bin', 'rb').read()
print(data)
print(data[4:8])
# ośmiobitowe bajty (znaki)
print(list(data))
# pierwszy argument to string formatujący
print(struct.unpack('>i4sh', data))
