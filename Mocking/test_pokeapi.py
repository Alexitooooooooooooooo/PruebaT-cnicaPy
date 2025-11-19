
import unittest
from unittest.mock import patch, MagicMock
from pokemon_api import get_pokemon_data

class TestPokeClient(unittest.TestCase):

    @patch('pokemon_api.requests.get')
    def test_get_name_pokemon(self, mock_get):
        mock_resp = mock_get.return_value
        mock_resp.json.return_value = {'name': 'bulbasaur'}

        name = get_pokemon_data(1)
        self.assertEqual(name, 'bulbasaur')
        mock_get.assert_called_once_with('https://pokeapi.co/api/v2/pokemon/1/')
        # Verifica que el nombre del Pokémon sea 'bulbasaur' con el id 1

if __name__ == '__main__':
    unittest.main()

#el mocking permitió aislar la lógica de la función y garantiza que responde correctamente ante cualquier situación simulada.