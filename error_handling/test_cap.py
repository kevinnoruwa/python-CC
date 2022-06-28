import unittest
import error_handling.cap as cap

# method needs test in front ex test_one_word
class TestCap(unittest.TestCase):
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')  
    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')      
    def test_is_another(self):
        text = 'cap cruch'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Cap Cruch')
        
        
        
        
        
if (__name__ == '__main__'):
    unittest.main()
        
        
    