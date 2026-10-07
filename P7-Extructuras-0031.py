# Rafael Emiliano Arevalo Murguia
# NC 0031
# P7 - Estructuras de decisión y repetición

print("Rafael Emiliano Arevalo Murguia - NC 0031")


# =========================
# IF - EJEMPLO 1
# =========================
print("+-+-+-+-+-+- IF - EJEMPLO 1 +-+-+-+-+-")
edad = 18

if edad >= 18:
    print("Es mayor de edad")


# =========================
# IF - EJEMPLO 2
# =========================
print("+-+-+-+-+- IF - EJEMPLO 2 +-+-+-+-+")
numero = 10

if numero > 5:
    print("El número es mayor que 5")


# =========================
# ELIF - EJEMPLO 1
# =========================
print("+-+-+-+-+- ELIF - EJEMPLO 1 +-+-+-+-+")
calificacion = 8

if calificacion >= 9:
    print("Excelente")
elif calificacion >= 6:
    print("Aprobado")


# =========================
# ELIF - EJEMPLO 2
# =========================
print("+-+-+-+- ELIF - EJEMPLO 2 +-+-+-+-+-")
numero = 0

if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("Es cero")


# =========================
# ELSE - EJEMPLO 1
# =========================
print("+-+-+-+-+- ELSE - EJEMPLO 1 +-+-+-+-+-")
edad = 15

if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")


# =========================
# ELSE - EJEMPLO 2
# =========================
print("+*+*+*+* ELSE - EJEMPLO 2 +*+*+*+*")
numero = 4

if numero % 2 == 0:
    print("Par")
else:
    print("Impar")


# =========================
# FOR - EJEMPLO 1
# =========================
print("+-+-+-+-+- FOR - EJEMPLO 1 +-+-+-+-+-+-")
for i in range(5):
    print(i)


# =========================
# FOR - EJEMPLO 2
# =========================
print("+-+-+-+-+-+- FOR - EJEMPLO 2 +-+-+-+-+-")
for nombre in ["Ana", "Luis", "Pedro"]:
    print(nombre)


# =========================
# WHILE - EJEMPLO 1
# =========================
print("+-+-+-+-+-+ WHILE - EJEMPLO 1 +-+-+-+-+-+")
contador = 1

while contador <= 5:
    print(contador)
    contador += 1


# =========================
# WHILE - EJEMPLO 2
# =========================
print("+-+-+-+-+-+ WHILE - EJEMPLO 2 +-+-+-+-+-+")
numero = 5

while numero > 0:
    print(numero)
    numero -= 1


print("==== Arevalo Rafael NC:0031 ====")