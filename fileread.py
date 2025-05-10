# file i/o
f = open ("./pk.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()
