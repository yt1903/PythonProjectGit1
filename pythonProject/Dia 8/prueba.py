import unittest
import cambia_texto


class ProbarCambiaTexto(unittest.TestCase):
    """
    unittest
    """
    def test_mayusculas(self):
        palabra = "Buen Dia"
        resultado = cambia_texto.todo_mayuscula(palabra)
        self.assertEqual(resultado, "bUEN DIA")


if __name__ == "__main__":
    unittest.main()