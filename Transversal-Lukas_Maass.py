def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Cupos por género")
    print("2. Búsqueda de películas por rango de precio")
    print("3. Actualizar precio de película")
    print("4. Agregar película")
    print("5. Eliminar película")
    print("6. Salir")
    print("=====================================")

def leer_opcion():
    while True:
        try:
            opcion = int(input(">"))
            if 1 <= opcion <=6 :
                return opcion
            else:
                print("Ingrese una Opcion Valida")
        except ValueError:
            print("\n Opcion no Valida, utilice Numeros")

def validar_texto_no_vacio(text):
    return len(text.strip()) > 0

def validar_Clasificacion(clasificacion):
    return clasificacion["A", "B", "C"]

def validar_es_3d(opcion):
    return opcion.lower() in ["si", "no"]


def validar_precio(precio):
    return precio > 0

def cupos(cupos):
    return cupos > 0

def validar_cupos(cupos):
    return cupos < 0

def buscar_codigo(cartelera_dict,codigo):
    buscar_codigo = codigo.upper().strip()
    return buscar_codigo in cartelera_dict


def cupos_genero(,cupos_genero,genero,codigo):
    cupos_totales = 0
    Genero_Buscado = genero.lower().strip()
    for datos in cupos_genero.items():
        if datos[1].lower() == Genero_Buscado:
            if datos in genero:
                cupos_totales += genero[datos][2]

def busqueda_precio_peliculas(peliculas_dict,cartelera_dict,p_min,p_max):
    resultados = []
    for codigo, datos_cartelera in cartelera_dict.items():
        precio = datos_cartelera[2]
        cupos = cartelera_dict[0]
        if p_min <= precio <=p_max and cupos > 0:
            nombre = peliculas_dict[codigo][0]
            resultados.append(f"{nombre}--{codigo}")
        if len(resultados) > 0:
            resultados.sort
            print("n\===Pelicula Encontrada===")
            for item in resultados:
                print(item)    
        else:
            print("\n===No se Encontraron Peliculas con esos Datos===")

def actualizar_precio(codigo,nuevo_precio):
    if buscar_codigo(codigo):
        codigo_limpio = codigo.upper().strip()
        codigo[codigo_limpio] = nuevo_precio
        return True
    return False

def eliminar_pelicula(peliculas,cartelera,codigo):
    if buscar_codigo(peliculas,codigo):
        codigo_limpio = codigo.upper().strip()
        del peliculas[codigo_limpio]
        del cartelera[codigo_limpio]
        return True
    return False

def Agregar_pelicula(codigo,titulo,genero,duracion,calsificacion,idioma,es_3d,precio,cupos):
    print

    
def main():
    peliculas = {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False],
}
    cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3],
}
    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            print("\nCupos Por Genero")
            cat = input("Ingrese la categoría a consultar: ")
            cupos_genero(peliculas, cartelera, cat)

        elif opcion ==2:
            print("\Búsqueda por Rango de Precio")
            try:
                p_min = int(input("Ingrese el precio mínimo: "))
                p_max = int(input("Ingrese el precio máximo: "))
                if p_min >= 0 and p_max >= p_min:
                    busqueda_precio_peliculas(peliculas,cartelera,p_min,p_max)
                else:
                    print("Ingrese los Datos de Manera Correcta")
            except ValueError:
                print("Datos Invalidos, Debe Ingresar Letras y Numeros")

        elif opcion == 3:
             print("\nActualizar Precio Pelicula")
             while True:
                codigo = input("Ingrese el codigo de la Pelicula: ")
                try:
                    nueva_pelicula = int(input("Ingrese el nuevo precio: "))
                    if validar_precio(nueva_pelicula):
                        if actualizar_precio(cartelera, cod, nueva_pelicula,):
                            print("Precio actualizado exitosamente.")
                        else:
                                print("El código ingresado no existe en el sistema.")
                    else:
                            print("El precio debe ser un número entero, mayor a cero.")
                except ValueError:
                        print("Entrada inválida. Debe ingresar un número entero válido para el precio.")
                    
                resp = input("\n¿Desea actualizar otro precio? (s/n): ")
                if resp.lower() != 's':
                    break

        elif opcion == 4:
            print("Agregar pelicula")
            codigo = input("Ingrese nuevo código: ")
            titulo = input("Nombre de la Pelicula: ")
            genero = input("Genero de la Pelicula: ").lower()
            duracion = input("Cunato dura la Pelicula: ")
            clasificacion = input("Que Clasificacion es la Pelicula (L/R/C): ").upper()
            idioma = input("Que Idioma Es?: ").lower()
            es_3d = input("es la Pelicula 3D? (s/n): ").lower
            precio = input("Precio?")
            cupos = input("Cuantos Cupos?")
            try:
                precio = int(input("Precio de venta: "))
                cupos = int(input("Unidades en Stock inicial: "))
                
                if (validar_texto_no_vacio(titulo) and validar_texto_no_vacio(genero) and 
                    validar_texto_no_vacio(duracion) and validar_Clasificacion(clasificacion) and 
                    validar_es_3d(es_3d) and validar_texto_no_vacio(idioma) and 
                    validar_precio(precio) and validar_cupos(cupos)):
                    
                    es_3d_bool = True if es_3d == 's' else False
                    peliculas = [titulo, genero, duracion, clasificacion, idioma, es_3d_bool]
                    cartelera = [precio, cupos]
                    
                    if Agregar_pelicula(titulo, genero, codigo, clasificacion, idioma, es_3d):
                        print("Pelicula Añadida con Exito.")
                    else:
                        print("El código ya existe. No se puede duplicar.")
                else:
                    print("Error: Uno o más datos no cumplen las Especificaciones.")
            except ValueError:
                print("Error: El precio y el Cupo deben ser Valores Numerios.")

        elif opcion == 5:
            print("Eliminar Pelicula")
            codigo = input("Ingrese el codigo de la Pelicula para Eliminar: ")
            if eliminar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d):
                print("La Pelicula Fue eliminada de Maenra Correcta.")
            else:
                print("El código no existe. No se pudo realizar la eliminación.")
                
        elif opcion == 6:
            print("Gracias por Elejir Nuestros Servicios!")
            break
if __name__ == "__main__":
    main()            
