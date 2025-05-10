# file i/o
f = open ("pk.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()

f = open ("pk.txt", "a")
f.write("testing that how write work in file i.o")
f.close()