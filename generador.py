import random
char = list("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
long = int(input("Longitud de la contraseña:"))
contr = []
for i in range(long):
    contr.append(random.choice(char))
print(contr)
