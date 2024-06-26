generos = ["Ficción", "No Ficción", "Ciencia"]

libros = []

ventas = []

def registrar_libro():
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    genero = input("Ingrese el género del libro (Ficción, No Ficción, Ciencia): ")
    while genero not in generos:
        print("Género no válido. Intente nuevamente.")
        genero = input("Ingrese el género del libro (Ficción, No Ficción, Ciencia): ")
    precio = float(input("Ingrese el precio del libro: "))
    libro = {"titulo": titulo, "autor": autor, "genero": genero, "precio": precio, "stock": 1}
    libros.append(libro)
    print("Libro registrado con éxito.")

def lista_libros():
    print("Lista de libros registrados:")
    for libro in libros:
        print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Género: {libro['genero']}, Precio: {libro['precio']}")

def registrar_venta():
    titulo = input("Ingrese el título del libro que desea vender: ")
    libro_encontrado = False
    for libro in libros:
        if libro["titulo"] == titulo:
            libro_encontrado = True
            cantidad = int(input("Ingrese la cantidad que desea vender: "))
            while cantidad > libro["stock"]:
                print("No hay suficiente stock disponible. Intente nuevamente.")
                cantidad = int(input("Ingrese la cantidad que desea vender: "))
            precio_por_unidad = libro["precio"]
            precio_final = cantidad * precio_por_unidad
            venta = {"titulo": titulo, "cantidad": cantidad, "precio_por_unidad": precio_por_unidad, "precio_final": precio_final}
            ventas.append(venta)
            libro["stock"] -= cantidad
            print("Venta registrada con éxito.")
            print("Boleta de venta:")
            print(f"Título: {titulo}, Cantidad: {cantidad}, Precio por unidad: {precio_por_unidad}, Precio final: {precio_final}")
            break
    if not libro_encontrado:
        print("Libro no encontrado en el inventario.")

def imprimir_reporte_ventas():
    print("Reporte de ventas:")
    genero_especifico = input("Ingrese el género que desea ver (Ficción, No Ficción, Ciencia) o presione Enter para ver todos: ")
    if genero_especifico:
        for venta in ventas:
            if venta["titulo"] in [libro["titulo"] for libro in libros if libro["genero"] == genero_especifico]:
                print(f"Título: {venta['titulo']}, Cantidad: {venta['cantidad']}, Precio por unidad: {venta['precio_por_unidad']}, Precio final: {venta['precio_final']}")
    else:
        for venta in ventas:
            print(f"Título: {venta['titulo']}, Cantidad: {venta['cantidad']}, Precio por unidad: {venta['precio_por_unidad']}, Precio final: {venta['precio_final']}")

def generar_txt():
    with open("ventas.txt", "w") as archivo:
        for venta in ventas:
            archivo.write(f"Título: {venta['titulo']}, Cantidad: {venta['cantidad']}, Precio por unidad: {venta['precio_por_unidad']}, Precio final: {venta['precio_final']}\n")
    print("Archivo txt generado con éxito.")

def main():
    while True:
        print("Menú:")
        print("1. Registrar libro")
        print("2. Listar todos los libros")
        print("3. Registrar venta")
        print("4. Imprimir reporte de ventas")
        print("5. Generar txt")
        print("6. Salir del programa")
        opcion = input("Ingrese la opción deseada: ")
        if opcion == "1":
            registrar_libro()
        elif opcion == "2":
            lista_libros()
        elif opcion == "3":
            registrar_venta()
        elif opcion == "4":
            imprimir_reporte_ventas()
        elif opcion == "5":
            generar_txt()
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    