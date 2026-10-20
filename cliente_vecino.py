# Cliente del servicio Envíos (equipo vecino) · Reto de integración
# Contrato del vecino: envios.proto · Qué hace y con qué datos probar: servicios/envios/README.md
# Antes de correrlo, el servidor del vecino debe estar corriendo (README.md, paso 5).
import grpc

import envios_pb2
import envios_pb2_grpc

canal = grpc.insecure_channel("localhost:50055")
stub = envios_pb2_grpc.EnviosStub(canal)

#`CotizarEnvio`: CP `28000`, 2500 g → 13900 centavos, 1 día<br>
#`Rastrear`: `GUIA-500` (4 estados) o `GUIA-501` (2)
###Dan error
#`CotizarEnvio`: CP `280` o peso `0`<br>
#`Rastrear`: `GUIA-999` |


print("=== Parte 1 · CotizarEnvio con un dato válido ===")
# TODO: arma la petición con un dato que funcione (tabla "Datos para probar" del README del vecino),
#       llama a stub.CotizarEnvio(...) e imprime los campos de la respuesta.
try:
    r = stub.CotizarEnvio(envios_pb2.CotizacionRequest(codigo_postal="28000", peso_gramos=2500))
    print(r)
except grpc.RpcError as e:
    print(f"Error: {e.code().name} - {e.details()}")

print("=== Parte 2 · CotizarEnvio con un dato que provoca error ===")
# TODO: llama con un dato que provoque error, dentro de try/except grpc.RpcError,
#       e imprime e.code() y e.details(). El programa NO debe tronar.
try:
    r = stub.CotizarEnvio(envios_pb2.CotizacionRequest(codigo_postal="280", peso_gramos=0))
    print(r)
except grpc.RpcError as e:
    print(f"Error: {e.code().name} - {e.details()}")




print("=== Parte 3 · Rastrear (streaming) ===")
print("Primer rastreo con timeout: ")
# TODO: recorre stub.Rastrear(...) con for e imprime cada caja en cuanto llegue.
#       Ponlo también dentro de try/except por si el servidor regresa un error.
print("Rastreo con menor tiempo de espera")
count = 0
try:
    for r in stub.Rastrear(envios_pb2.GuiaRequest(guia="GUIA-500"),timeout= 2):
        print(f"Llegó: Número de guía: {r.guia} - Estado: {r.estado} - Lugar: {r.lugar}")
        count += 1
except grpc.RpcError as e:
    print(f"Recibí {count} cajas del rastreo de la guía GUIA-500")
    print(f"Error: {e.code().name} - {e.details()}")

print ("Rastreo con mayor tiempo de espera")
count = 0
try:
    for r in stub.Rastrear(envios_pb2.GuiaRequest(guia="GUIA-500"),timeout=5):
        print(f"Llegó: Número de guía: {r.guia} - Estado: {r.estado} - Lugar: {r.lugar}")
        count += 1
    print(f"Recibí {count} cajas del rastreo de la guía GUIA-500")
except grpc.RpcError as e:
    print(f"Error: {e.code().name} - {e.details()}")

print("Segundo rastreo: ")
try:
    for r in stub.Rastrear(envios_pb2.GuiaRequest(guia="GUIA-501")):
        print(f"Llegó: Número de guía: {r.guia} - Estado: {r.estado} - Lugar: {r.lugar}")
except grpc.RpcError as e:
    print(f"Error: {e.code().name} - {e.details()}")

print("Tercer rastreo: ")
try:
    for r in stub.Rastrear(envios_pb2.GuiaRequest(guia="GUIA-999"), ):
        print(f"Llegó: Número de guía: {r.guia} - Estado: {r.estado} - Lugar: {r.lugar}")
except grpc.RpcError as e:
    print(f"Error: {e.code().name} - {e.details()}")
