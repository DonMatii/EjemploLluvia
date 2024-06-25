nombreLibro = ["holitas"]
genero = ["ciencia", "ficcion", "no ficcion"]
autorLibro = ["matii"]
precio = [9000]
venta = [0]

while True:
    
    print("Bienvenido, ingresa una de las opciones para comenzar: \n ")
    print("1. Registra un libro con su autor, el género y el precio ")
    print("2. Listar todos los libros ")
    print("3. Registrar venta ")
    print("4. Imprimir reporte de ventas ")
    print("5. Generar archivo de texto con la información de las ventas del día por género. (presiona ENTER para mostrar todos los generos)")
    print("6. Salir del Programa\n")
    
    try:
            seleccion = int(input("Ingrese una opción valida: "))

            if seleccion == 1:
                
                nombreLibro = input("Ingresa un libro a agegar: ").lower()
                autorLibro = input("Ingresa el autor del libro: ").lower()
                genero = input("Ingresa el genero del libro (ficción, no ficción, ciencia): ").lower()
                precio = int(input("Ingrese el precio del libro: "))

                print(f"\nlos libros ingresados son, titulos: {nombreLibro}, autores: {autorLibro}, genero: {genero} y el precio es de ${precio}\n")
                

            elif seleccion == 2:
                print(f"Los libros que hay en la colección son: {nombreLibro}")
                print()

            elif seleccion == 3:
                venta = int(input("Ingresa tu venta en números: "))
                

            elif seleccion == 4:
                print(f"tus ventas actuales son: {venta}")

            elif seleccion == 5:
                print("\nSaliendo del sistema, Gracias por su preferencia!\n")
                break

    except ValueError:
        print("opcion no valida, intentelo de nuevo.")


