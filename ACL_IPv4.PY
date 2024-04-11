def tipo_acl(numero_acl):
    # Verificar si el número de ACL IPv4 es estándar, extendida o no corresponde
    if numero_acl >= 1 and numero_acl <= 99:
        return "Estándar"
    elif numero_acl >= 100 and numero_acl <= 199:
        return "Extendida"
    else:
        return "El número no corresponde a una lista de acceso"

def main():
    # Solicitar al usuario que ingrese el número de ACL IPv4
    numero_acl = int(input("Ingrese el número de ACL IPv4: "))

    # Determinar el tipo de ACL IPv4
    tipo = tipo_acl(numero_acl)

    # Imprimir el resultado
    print("Tipo de ACL IPv4:", tipo)

if __name__ == "__main__":
    main()
