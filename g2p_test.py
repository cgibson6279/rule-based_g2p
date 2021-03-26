"""Unit tests for Portuguese G2P."""

import unittest

import g2p


class G2PTest(unittest.TestCase):
    def rewrites(self, istring: str, expected_ostring: str) -> None:
        """Asserts that the g2p rule produces the correct output.

        Note that this itself is not a unit test because its name does not
        begin with `test_`; but it can be used to implement other unit tests.

        Args:
            istring: the input string
            expected_ostring: the expected output string.
        """
        ostring = g2p.g2p(istring)
        self.assertEqual(ostring, expected_ostring)

    def test_vez(self):
        self.rewrites("cases", "kazis")
        self.rewrites("cimento", "simentu")
        self.rewrites("chato", "ʃatu")
        self.rewrites("casa", "kaza")
        self.rewrites("filho", "fiʎu")
        self.rewrites("homem", "omem")
        self.rewrites("ninho", "niɲu")
        self.rewrites("vez", "ves")
        # stretch goal
        self.rewrites("árvore", "arvuɾi")
        self.rewrites("braço", "bɾasu")
        self.rewrites("carro", "kaʁu")
        self.rewrites("interesse", "inteɾesi")
        self.rewrites("partes", "paɾtʃis")
        self.rewrites("rápido", "ʁapidu")
        self.rewrites("verdade", "veɾdadʒi")


if __name__ == "__main__":
    unittest.main()
