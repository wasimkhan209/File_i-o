# file i/o
# f = open ("pk.txt", "r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# f = open ("pk.txt", "a")
# f.write("Please Test that how write work in file i.o")
# f.close()

f = open("pk.txt", "a")
f.write("Testing again and again coz to clear the concept")
f.close()

with open("newpractice.txt" , "a+") as f:
    f.write("Hi, everyone \n" + "i'm learning python \n" + "so, i'm very excited for learning python \n" + "Thanks to all of you")