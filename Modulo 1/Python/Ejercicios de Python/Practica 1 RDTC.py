#Ejercicio 1
Saludo = "Hola mi nombre es"
Nombre = "Ronald mTrujillo"
print(Saludo,Nombre)

#Ejercicio 2
A = 10
B = 20
SUMA = A + B 
print(SUMA)

#Ejercicio 3
Usuario =input("ingresa tu nombre")
print(f"Hola mi nombre es {Usuario}")

#Ejercicio 4
Comida_Favorita = "Hamburguesas"
print(Comida_Favorita)

#Ejercicio 5
C = 5
D = 15
RESTA = C - D 
print(RESTA)

#Ejercicio 6
Edad = input("Cuantos años tienes")
print(f"Tu edad es {Edad}")

#Ejercicio 8
numero1 = 3
numero2 = 4
MULTIPLICACION = numero1 * numero2 
print(MULTIPLICACION)

#Ejercicio 9
Color =input("ingresa tu Color Favorito")
print(f"¡Qué buen gusto! El {Color} es genial.")

#Ejercicio 10
from playsound import playsound

def mostrar_letra_con_sonido():
    letra = """
    In this farewell
    There's no blood, there's no alibi
    'Cause I've drawn regret
    From the truth of a thousand lies...
    """
    print("🎵 Letra de 'What I've Done' - Linkin Park 🎵\n")
    print(letra)

    # Reproduce el archivo de sonido (debe estar en la misma carpeta que este script)
    playsound("what_ive_done.mp3")

# Ejecutar la función
mostrar_letra_con_sonido()

