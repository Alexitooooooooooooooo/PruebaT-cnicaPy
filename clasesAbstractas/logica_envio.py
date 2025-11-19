from envio import Envio

class EnvioTerrestre(Envio):
    def __init__(self, distancia_km, peso_kg):
        self.distancia_km = distancia_km
        self.peso_kg = peso_kg
        self.tipo = "Terrestre"

    def calcular_costo(self):
        return 50 + (self.distancia_km * 0.5) + (self.peso_kg * 2)

class EnvioAereo(Envio):
    def __init__(self, distancia_km, peso_kg):
        self.distancia_km = distancia_km
        self.peso_kg = peso_kg
        self.tipo = "Aereo"

    def calcular_costo(self):
        return 150 + (self.distancia_km * 2) + (self.peso_kg * 5)

def procesar_envios(lista_de_envios):
    for envio in lista_de_envios:
           costo = envio.calcular_costo()
           print(f"Tipo de envío: {envio.tipo}, Costo del envío: {costo:.1f}$")

def obtener_datos_envio():
    lista_input = []

    for i in range(2):
        tipo = input("Ingrese el tipo de envío (terrestre/aereo): ").strip().lower()
        distancia = float(input("Ingrese la distancia en km: "))
        peso = float(input("Ingrese el peso en kg: "))

        if tipo == "terrestre":
            envio = EnvioTerrestre(distancia, peso)
        elif tipo == "aereo":
            envio = EnvioAereo(distancia, peso)
        else:
            print("Tipo de envío no válido. Intente de nuevo.")
            continue

        lista_input.append(envio)

    return lista_input

if __name__ == "__main__":
    envios = [
        EnvioTerrestre(100, 10),
        EnvioAereo(500, 5),
        EnvioTerrestre(50, 2),
        EnvioAereo(200, 20)
    ]
    procesar_envios(envios)

    envios_usuario = obtener_datos_envio()
    procesar_envios(envios_usuario)