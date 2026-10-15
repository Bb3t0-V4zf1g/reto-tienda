# Nuestro equipo

- **Nuestro servicio:** Notificaciones · puerto 50054 · contrato `notificaciones.proto`
- **Servicio que consumimos (vecino):** Envíos · puerto 50055 · contrato `envios.proto`
- **Repositorio del equipo vecino:** https://github.com/s4idl/EnviosPagosEquipo2

| Integrante | Matrícula | Rol |
| Lorenzo Sebastián Chavéz Rodriguez | 20209634 | Servidor |
| Alberto Vazquez Figueroa| 20204735 | Cliente |
| Mayte Muñoz Rosales| 20201073 | Integración (README, issues y prueba cruzada) |

## Prueba cruzada

Corran `python cliente_vecino.py` contra el servidor **real** del equipo vecino (el que clonaron en `../vecino`)
y peguen aquí todo lo que imprimió:

```
=== Parte 1 · CotizarEnvio con un dato válido ===
Error: UNAVAILABLE - failed to connect to all addresses; last error: UNKNOWN: ipv4:127.0.0.1:50055: Failed to connect to remote host: Connection refused
=== Parte 2 · CotizarEnvio con un dato que provoca error ===
Error: UNAVAILABLE - failed to connect to all addresses; last error: UNKNOWN: ipv4:127.0.0.1:50055: Failed to connect to remote host: Connection refused
=== Parte 3 · Rastrear (streaming) ===
Error: UNAVAILABLE - failed to connect to all addresses; last error: UNKNOWN: ipv4:127.0.0.1:50055: Failed to connect to remote host: Connection refused
```

## Issues

Enlaces a los issues que abrieron en el repositorio del vecino o que les abrieron a ustedes (si hubo):

-

## Uso de IA (Acuerdo No. 23/2024 UdeC)

¿Usaron IA? ¿Cuál, quién y para qué? (por ejemplo: "Copilot para el for de la parte 3; lo revisamos línea por línea").

-
