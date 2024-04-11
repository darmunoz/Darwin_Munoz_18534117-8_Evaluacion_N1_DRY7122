# Definición de las VLANs para cada switch según el diagrama de referencia
switch1_vlans = [10, 20, 30]
switch1_native_vlan = 99

switch2_vlans = [40, 50, 60]
switch2_native_vlan = 200

# Función para verificar si una VLAN está presente en un conjunto de VLANs
def verificar_vlan(vlan, vlans):
    return vlan in vlans

# Función para realizar la comparación y mostrar los resultados
def comparar_switches(nombre_switch, native_vlan, vlans_referencia, vlans_switch):
    print(f"Comparación para el {nombre_switch}:")
    
    print(f"Verificando VLANs en el {nombre_switch}:")
    for vlan in vlans_referencia:
        if verificar_vlan(vlan, vlans_switch):
            print(f"VLAN {vlan} está presente en el {nombre_switch}")
        else:
            print(f"VLAN {vlan} no está presente en el {nombre_switch}")

    print(f"Comparando native VLAN del {nombre_switch}...")
    if native_vlan == 99:
        if native_vlan in vlans_switch:
            print("La native VLAN es igual a la VLAN creada en el switch")
        else:
            print("La native VLAN es diferente a la VLAN creada en el switch")
    else:
        print("La native VLAN es diferente a la VLAN creada en el switch")

# Comparación para el switch1
comparar_switches("switch1", switch1_native_vlan, [10, 100, 30], switch1_vlans)

# Comparación para el switch2
comparar_switches("switch2", switch2_native_vlan, [40, 50, 60], switch2_vlans)
