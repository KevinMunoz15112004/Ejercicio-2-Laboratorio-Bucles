print("--------------si desea finalizar la compra presione 0----------- ")

num_articulos = int(input("Ingrese la cantidad de artículos: "))
costo_total = 0
descuento_total = 0
precio_articulo=0
if precio_articulo >= 200:
        descuento = 0.15
elif 100 < precio_articulo < 200:
        descuento = 0.12
else:
        descuento = 0.10

for i in range(num_articulos):
    precio_articulo = float(input(f"Ingrese el precio del artículo  {i + 1}  : ")) 
    costo_con_descuento = precio_articulo * (1 - descuento)
    costo_total += costo_con_descuento
    descuento_total += precio_articulo - costo_con_descuento
    
    print(f"Artículo {i + 1}: Costo = ${round(costo_con_descuento, 2)}, Descuento = ${round(precio_articulo - costo_con_descuento, 2)}")

    if precio_articulo == 0:
        break

    print("-------------------------------------------------------------------------------")
if precio_articulo == 0:
    print(f"Monto tota l a pagar por {num_articulos} artículos: ${costo_total:.2f}")
    print(f"Descuento total: ${descuento_total:.2f}")
    print ("muchas gracias")
    
