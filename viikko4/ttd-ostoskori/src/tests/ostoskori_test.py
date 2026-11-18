import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def _assert_kori_tyhjia(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(len(self.kori.ostokset()), 0)

    def test_ostoskori_on_alussa_tyhjia(self):
        self._assert_kori_tyhjia()

    def test_yhden_tuotteen_lisaaminen_luo_yhden_ostoksen(self):
        tuote = Tuote("Maito", 3)
        self.kori.lisaa_tuote(tuote)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        self.assertEqual(ostokset[0].tuotteen_nimi(), tuote.nimi())
        self.assertEqual(ostokset[0].lukumaara(), 1)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_eri_tuotteen_lisaaminen_luo_kaksi_ostosta(self):
        self.kori.lisaa_tuote(Tuote("Maito", 3))
        self.kori.lisaa_tuote(Tuote("Juusto", 5))

        self.assertEqual(len(self.kori.ostokset()), 2)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
        self.assertEqual(self.kori.hinta(), 8)

    def test_saman_tuotteen_kaksi_lisaamista_kasvattaa_yhden_ostoksen_maaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        self.assertEqual(ostokset[0].tuotteen_nimi(), maito.nimi())
        self.assertEqual(ostokset[0].lukumaara(), 2)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
        self.assertEqual(self.kori.hinta(), 6)

    def test_saman_tuotteen_yhden_kappaleen_poistaminen_jattaa_yhden(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.kori.poista_tuote(maito)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        self.assertEqual(ostokset[0].lukumaara(), 1)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
        self.assertEqual(self.kori.hinta(), 3)

    def test_ainoan_tuotteen_poistaminen_tyhjentaa_ostoskorin(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.kori.poista_tuote(maito)

        self._assert_kori_tyhjia()

    def test_tyhjenna_tyhjentaa_ostoskorin(self):
        maito = Tuote("Maito", 3)
        juusto = Tuote("Juusto", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(juusto)

        self.kori.tyhjenna()

        self._assert_kori_tyhjia()