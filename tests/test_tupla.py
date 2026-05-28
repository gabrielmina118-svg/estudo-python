import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from funcao.tupla import calcular_preco_final, imposto_explosivo, imposto_sp


class TestImpostoSp(unittest.TestCase):
    def test_importado(self):
        self.assertEqual(imposto_sp(True), 0.15)

    def test_nacional(self):
        self.assertEqual(imposto_sp(False), 0.05)


class TestImpostoExplosivo(unittest.TestCase):
    def test_explosivo_fator_padrao(self):
        self.assertEqual(imposto_explosivo(True), 0.11)

    def test_explosivo_com_fator(self):
        self.assertEqual(imposto_explosivo(True, 2), 0.22)

    def test_nao_explosivo(self):
        self.assertEqual(imposto_explosivo(False), 0)
        self.assertEqual(imposto_explosivo(False, 3), 0)


class TestCalcularPrecoFinal(unittest.TestCase):
    def test_com_imposto_sp(self):
        self.assertAlmostEqual(
            calcular_preco_final(150, imposto_sp, True), 150.15
        )

    def test_com_imposto_explosivo(self):
        self.assertAlmostEqual(
            calcular_preco_final(150.15, imposto_explosivo, True, 2), 150.37
        )

    def test_fluxo_completo(self):
        preco_bruto = 150
        preco_medio = calcular_preco_final(preco_bruto, imposto_sp, True)
        preco_final = calcular_preco_final(
            preco_medio, imposto_explosivo, True, 2
        )

        self.assertAlmostEqual(preco_medio, 150.15)
        self.assertAlmostEqual(preco_final, 150.37)


if __name__ == "__main__":
    unittest.main()
