import time
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}

def stock_marca(marca):
    total_stock = 0
    marca_lower = marca.lower()
    for key, value in productos.items():
        value_lower = value[0].lower()
        if marca_lower == value_lower:
            total_stock += stock[key][1]
    print(f"El stock para la marca {marca} es: {total_stock}.")
    time.sleep(2)

def busqueda_precio(p_min, p_max):
    items_dic = []
    items_flag = 0

    for key, value in stock.items():
        # Si hay stock
        if value[1] > 0:
            precio = value[0]
            if p_min <= precio <= p_max:
                items_dic.append(f"{productos[key][0]}--{key}")
                items_flag += 1

    # Si hay items en el rango
    if items_flag > 0:
        print(f"Los notebooks con stock entre los precios consultados son: {items_dic}")
        time.sleep(2)
    else:
        print("No hay notebooks en ese rango de precios.")
        time.sleep(2)

def actualizacion_precio(modelo, precio):
    modelo_lower = modelo.lower()
    change_flag = 0
    for key in stock:
        key_lower = key.lower()
        if modelo_lower == key_lower:
            change_flag += 1
            stock[key][0] = precio

    if change_flag > 0:
        return True
    else:
        return False

def main():
    while True:
        print("\n***MENU PRINCIPAL***")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Actualizar precio.")
        print("4. Salir.")
        op = input("Ingrese su opción: ")
        if op == "1":
            marca = input("\nIngrese marca a consultar: ")
            stock_marca(marca)
        elif op == "2":
            while True:
                try:
                    precio_min = int(input("Ingrese precio mínimo: "))
                    if precio_min >= 0:
                        break
                    else:
                        print("Por favor ingresa precio mínimo positivo.")
                        time.sleep(2)
                        continue
                except ValueError:
                    print("Por favor ingresa precio mínimo con valores enteros.")
                    time.sleep(2)
            while True:
                try:
                    precio_max = int(input("Ingrese precio máximo: "))
                    break
                except ValueError:
                    print("Por favor ingresa precio máximo con valores enteros.")
                    time.sleep(2)
            busqueda_precio(precio_min, precio_max)
        elif op == "3":
            option_flag = True
            while True:
                if option_flag == True:
                    modelo = input("\nIngrese modelo a actualizar: ")
                    while True:
                        try:
                            new_price = int(input("Ingrese precio nuevo: "))
                            break
                        except ValueError:
                            print("Por favor ingrese valores enteros.")
                            time.sleep(2)
                    # Retorno true o false si se actualizó el código
                    is_actualiced = actualizacion_precio(modelo, new_price)
                    if is_actualiced == True:
                        print("Precio actualizado correctamente.")
                        time.sleep(2)
                    else:
                        print(f"|!| El modelo '{modelo}' no existe, no pudimos actualizar el precio.")
                        time.sleep(2)
                    while True:
                        op_change = input("\nDesea actualizar otro precio (s/n)?: ").lower()
                        if op_change == "s" or op_change == "si" or op_change == "sí":
                            break
                        elif op_change == "n" or op_change == "no":
                            option_flag = False
                            break
                        else:
                            print("Por favor selecciona (s/n)")
                            time.sleep(2)
                else:
                    break
        elif op == "4":
            print("Programa finalizado.")
            time.sleep(2)
            exit()
        else:
            print("Por favor ingresa una opción válida.")
            time.sleep(2)

main()


# Link repositorio:
# https://github.com/ErikDuoc/evaluacion_final