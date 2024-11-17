import unittest
import cup

class TestCup(unittest.TestCase):
    def test_one_word(self):
        text = 'python'
        result = cup.cap_text(text)
        self.assertEqual(result, 'Python')
    
    def test_mult_words(self):
        text = 'monty python'
        result = cup.cap_text(text)
        
        self.assertEqual(result, 'Monty Python')
        
if __name__ == '__main__':
    unittest.main()