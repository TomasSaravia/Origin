def redondear_numero(numero):
    if numero - int(numero) > 0.50:
        print(int(numero) + 1)
    else:
        print(int(numero))

