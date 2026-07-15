# 🔍 SOC Log Analyzer — SSH Brute Force Detector

## ¿Qué hace?
Script Python que analiza logs de autenticación Linux 
y detecta ataques de fuerza bruta SSH automáticamente.

## ¿Por qué lo hice?
En un SOC real un analista puede recibir alertas sobre 
servidores con miles de líneas de logs. Revisar todo 
manualmente toma horas. Este script lo hace en segundos.

## ¿Qué detecta?
- Intentos fallidos de login SSH
- IPs atacantes ordenadas por cantidad de intentos
- Logins exitosos después de intentos fallidos
- Genera reporte con recomendación de acción

## Ejemplo de output
🚨 IPs sospechosas detectadas:
185.234.1.5  → 6 intentos fallidos
45.33.32.156 → 2 intentos fallidos
🚨 ALERTA CRÍTICA: Hubo acceso exitoso
Escalar a senior inmediatamente
## Herramientas usadas
- Python 3
- Linux auth.log

## Autor
Josue — SOC Analyst Junior	
