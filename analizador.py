# Analizador de logs SSH - SOC portafolio
# Dectecta ataques de fuerza bruta en auth.log


print("Iniciando analizador de logs SSH...")

# Abrir el archivo de logs
archivo = open("auth.log","r")

# Leer todas las lineas
lineas = archivo.readlines()

print(f"Total de lineas en el log: {len(lineas)}")

# Detectar intento fallidos
intentos_fallidos = []

for linea in lineas:
    if "Failed password" in linea:
        intentos_fallidos.append(linea)


print(f"Intentos fallidos encontrados: {len(intentos_fallidos)}")

# Contar intentos por IP
ips = {}


for linea in intentos_fallidos:
    partes = linea.split()
    ip = partes[10]

    if ip in ips:
        ips[ip] +=1
    else:
        ips[ip] = 1


# Mostrar resultados
print("\n IPs sospechosas detectadas:")
for ip, cantidad in sorted(ips.items(), key=lambda x: x[1], reverse=True):
    print(f" {ip} {cantidad} intentos fallidos")

# Detectar logins exitosos
print("\n Logins exitosos:")
exitosos = []

for linea in lineas:
    if "Accepted password" in linea :
        exitosos.append(linea) 
        partes = linea.split()
        ip = partes[10]
        print(f" Login exitoso desde: {ip}")


if len(exitosos) == 0:
    print(" Ninguno detectado")

# Reporte final
print("\n" + "="*40)
print("REPORTE FINAL")
print("="*40)
print(f"Total líneas analizadas: {len(lineas)}")
print(f"Intentos fallidos: {len(intentos_fallidos)}")
print(f"IPs atacantes detectadas: {len(ips)}")
print(f"Logins exitosos: {len(exitosos)}")

if len(exitosos) > 0:
    print("\n🚨 ALERTA CRÍTICA: Hubo acceso exitoso")
    print("   Escalar a senior inmediatamente")
else:
    print("\n✅ Sin acceso exitoso detectado")
    print("   Recomendar bloqueo de IPs en firewall")

print("="*40)
