import unittest
import re
from python_generator_short_code import generator_short_code


class GeneratorTests(unittest.TestCase):

    def test_001_basic_generation(self):
        code = generator_short_code()
        self.assertEqual(len(code), 6)
        code = generator_short_code(length=12)
        self.assertEqual(len(code), 12)

    def test_002_upper(self):
        code = generator_short_code(case='upper')
        self.assertEqual(code, code.upper())

    def test_003_lower(self):
        code = generator_short_code(case='lower')
        self.assertEqual(code, code.lower())

    def test_004_only_letter(self):
        code = generator_short_code(_digits=False)
        self.assertFalse(bool(re.search(r'\d', code)))

    def test_005_only_digits(self):
        code = generator_short_code(_letters=False)
        self.assertFalse(bool(re.search(r'[a-zA-Z]', code)))

    def test_006_punctuation(self):
        code = generator_short_code(_letters=False, _digits=False, _punctuation=True)
        self.assertTrue(
            bool(re.search(r"""[!#"$%&'()*+,-./:;<=>?@[\]^_`{|}~]""", code)))

if __name__ == '__main__':
    unittest.main()
