print("resident evil 6")

opcion = input("que eliges(INICIAR/EXIT):").strip().upper()
opcion = input("que personaje eliges (LEON/CHRIS)")

if opcion == "LEON":
    print("\nescojes a leon vas directo al pueblo a rescartar a la hija del presidente vas en direccion al pueblo?")
    
    opcion = input("¿Qué haces? (INVESTIGAR/IGNORAR): ")
    
    if opcion == "INVESTIGAR":
        print("\nvas al pueblo encuantras una multitud ellos te atacan que haces")
    elif opcion == "IGNORAR":
        print("\nDecides ignorar el pueblo la hija del presidente muere . Fin del juego.")
    else: 
        print("\nNo elegiste una opción IGNORAR. Fin del juego.")
    
    opcion = input( "que haces (ATACAR/CORRER)")
    
    if opcion == "ATACAR":
        print("\nte abres paso hacia el cautiverio de la hija de presidente y la salvas .fin del juego")
    elif opcion == "CORRER":
        print("\nun aldeano te soprende con una motosierra y te parte por la mitad . Fin del juego.")
    else: 
        print("\nNo elegiste una opción válida. Fin del juego.")
   
elif opcion == "CHRIS":
    print("\nescojes a Chris  llegas a africa descubres que albert w quiere apoderarse del mundo. ¿Quieres huir o enfrentarte a el?")
    
    opcion = input("¿Qué haces? (HUIR/ENFRENTAR): ").strip().upper()

    if opcion == "HUIR":
        print("\nEscapas y albert w gana. Fin del juego.")
    elif opcion == "ENFRENTAR":
        print("\nDecides retarlo y ganas evitando el fin del mundo. Fin del juego.")
    else:
        print("\nNo elegiste una opción válida. Fin del juego.")

