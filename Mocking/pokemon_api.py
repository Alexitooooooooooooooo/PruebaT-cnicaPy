#El Mocking es utilizado para simular el comportamiento de objetos complejos o externos en pruebas unitarias.
# Permite crear objetos ficticios que imitan la interfaz y el comportamiento de los objetos reales, facilitando la prueba de componentes individuales sin depender de sus dependencias externas.    

import requests

def get_pokemon_data(pokemon_id):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/'
    response = requests.get(url)
    data = response.json()
    return data['name']