import unittest
from unittest.mock import Mock
from kauppa import Kauppa
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 42
        self.varasto_mock = Mock()
        self.varasto_mock.saldo.side_effect = {1: 10, 2: 10, 3: 0}.get
        self.varasto_mock.hae_tuote.side_effect = {
            1: Tuote(1, "maito", 5),
            2: Tuote(2, "leipä", 3),
            3: Tuote(3, "Olut", 4),
        }.get
        self.kauppa = Kauppa(
            self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock
        )
        self.kauppa.aloita_asiointi()

    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called()

    def test_maksettaessa_tilisiirto_kutsuu_oikeilla_parametreilla(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 5
        )

    def test_pystyy_ostaa_kahta_eri_tuotetta(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 8
        )

    def test_ostetaan_kaksi_samaa_tuotetta(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 10
        )

    def test_ostetaan_loppuunmyynty_tuote(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 5
        )
