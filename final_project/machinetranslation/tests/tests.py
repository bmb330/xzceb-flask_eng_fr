import unittest
from translator import english_to_french, french_to_english

class TestTranslatorMethods(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        with self.assertRaises(TypeError):
            english_to_french()
        
    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        with self.assertRaises(TypeError):
            french_to_english()

if __name__ == '__main__':
    unittest.main()
