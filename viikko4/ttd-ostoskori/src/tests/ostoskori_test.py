import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(Tuote("Maito", 3))
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_hinta_sama_kuin_tuotteen(self):
        self.kori.lisaa_tuote(Tuote("Maito", 3))
        self.assertEqual(self.kori.hinta(), 3)

    def test_kaksi_eri_tuotetta_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(Tuote("Maito", 3))
        self.kori.lisaa_tuote(Tuote("Juusto", 5))
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kaksi_eri_tuotetta_hinta_on_summa(self):
        self.kori.lisaa_tuote(Tuote("Maito", 3))
        self.kori.lisaa_tuote(Tuote("Juusto", 5))
        self.assertEqual(self.kori.hinta(), 8)

    def test_kaksi_samaa_tuotetta_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kaksi_samaa_tuotetta_hinta_kaksinkertainen(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 6)