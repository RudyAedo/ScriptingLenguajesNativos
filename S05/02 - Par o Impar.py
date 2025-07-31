def ParImpar(numero):
  
    # % devuelve el residuo de un número
    # En este ejemplo el residuo del número dividido sobre 2
    if numero % 2 == 0:
        return "Es par"
    else:
        return "Es impar"

print(ParImpar(10))
print(ParImpar(7))
