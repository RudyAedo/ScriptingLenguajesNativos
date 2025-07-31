def miProc(A, B):
    if A == B:
        return "Son iguales"
    else:
        return "Son diferentes"

# Prueba del procedimiento
resultado = miProc(5, 5)
print(resultado)  # Salida: Son iguales

resultado = miProc(3, 7)
print(resultado)  # Salida: Son diferentes
