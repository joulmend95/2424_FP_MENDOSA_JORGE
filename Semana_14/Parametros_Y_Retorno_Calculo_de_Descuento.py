def calcular_descuento(monto_total_de_compra, descuento=0.10):
    # Calcula el monto de descuento aplicando el porcentaje de descuento al monto total de la compra
    monto_de_descuento = monto_total_de_compra * descuento
    return monto_de_descuento  # Devuelve el monto de descuento calculado

# Llama a la función con un monto total de $960 y el descuento predeterminado del 10%
descuento_aplicado = calcular_descuento(960)

# Llama a la función con un monto total de $1100 y un descuento del 25%
descuento_aplicado2 = calcular_descuento(1100, 0.25)

# Calcula el total a pagar restando el descuento aplicado del monto total de la primera compra
total_a_pagar = 960 - descuento_aplicado

# Calcula el total a pagar restando el descuento aplicado del monto total de la segunda compra
total_a_pagar_2 = 1100 - descuento_aplicado2

# Imprime el monto de descuento y total a pagar para la primera compra
print("Monto de descuento con el 10% de $960: ", descuento_aplicado)
print("Total a pagar de la primera compra de $960: ", total_a_pagar)

# Imprime el monto de descuento y total a pagar para la segunda compra
print("Monto de descuento con el 25% de $1100: ", descuento_aplicado2)
print("Total a pagar de la segunda compra de $1100: ", total_a_pagar_2)

