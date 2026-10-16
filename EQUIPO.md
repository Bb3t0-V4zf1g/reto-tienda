# Nuestro equipo

- **Nuestro servicio:** Notificaciones · puerto 50054 · contrato `notificaciones.proto`
- **Servicio que consumimos (vecino):** Envíos · puerto 50055 · contrato `envios.proto`
- **Repositorio del equipo vecino:** https://github.com/s4idl/EnviosPagosEquipo2

| Integrante | Matrícula | Rol |
| Lorenzo Sebastián Chavéz Rodriguez | 20209634 | Servidor e Integración (Prueba Cruzada) |
| Alberto Vazquez Figueroa| 20204735 | Cliente y Pruebas (Probar si los datos que devuelve el servidor del vecino sean correctos) |
| Mayte Muñoz Rosales| 20201073 | Servidor y Documentación (README) |

## Prueba cruzada

Corran `python cliente_vecino.py` contra el servidor **real** del equipo vecino (el que clonaron en `../vecino`)
y peguen aquí todo lo que imprimió:

```
=== Parte 1 · CotizarEnvio con un dato válido ===
=== Parte 1 · CotizarEnvio con un dato válido ===
costo_centavos: 13900
dias: 1

=== Parte 2 · CotizarEnvio con un dato que provoca error ===
Error: INVALID_ARGUMENT - Código postal de 5 dígitos y peso mayor a 0
=== Parte 3 · Rastrear (streaming)===
Primer rastreo: 
Llegó: Número de guía: GUIA-500 - Estado: Recibido - Lugar: Colima
Llegó: Número de guía: GUIA-500 - Estado: En bodega - Lugar: Colima
Llegó: Número de guía: GUIA-500 - Estado: En camino - Lugar: Manzanillo
Llegó: Número de guía: GUIA-500 - Estado: Entregado - Lugar: Manzanillo
Segundo rastreo: 
Llegó: Número de guía: GUIA-501 - Estado: Recibido - Lugar: Colima
Llegó: Número de guía: GUIA-501 - Estado: En camino - Lugar: Guadalajara
Tercer rastreo: 
Error: NOT_FOUND - La guía GUIA-999 no existe
```

## Issues

Enlaces a los issues que abrieron en el repositorio del vecino o que les abrieron a ustedes (si hubo):

-

## Uso de IA (Acuerdo No. 23/2024 UdeC)

¿Usaron IA? ¿Cuál, quién y para qué? (por ejemplo: "Copilot para el for de la parte 3; lo revisamos línea por línea").
Copilot para que nos indique como entrar en un entorno virtual debido a que en el momento que ejecutamos "bash compilar.sh" se nos arroja un error acerca del modulo grpc.

Estos fueron los comandos que nos proporcionó:
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
-
