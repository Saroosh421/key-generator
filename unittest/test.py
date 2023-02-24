import string
import unittest
from key_generator import generate

class TestGenerate(unittest.TestCase):
    
    def test_default_key(self):
        # Generate default key, 5 atoms with '-' separator
        key = generate().get_key()
        self.assertIsInstance(key, str)
        self.assertEqual(key.count('-'), 4)
        atoms = key.split('-')
        for atom in atoms:
            self.assertGreaterEqual(len(atom), 3)
            self.assertLessEqual(len(atom), 10)
            self.assertRegex(atom, '^[0-9a-fA-F]*$')
    
    def test_custom_key(self):
        # Generate custom key with 5 atoms, ':' separator, min length 1, max length 2, lowercase letters
        key = generate(num_of_atom=5, separator=':', min_atom_len=1, max_atom_len=2, type_of_value='char', capital='none').get_key()
        self.assertIsInstance(key, str)
        self.assertEqual(key.count(':'), 4)
        atoms = key.split(':')
        for atom in atoms:
            self.assertGreaterEqual(len(atom), 1)
            self.assertLessEqual(len(atom), 2)
            self.assertRegex(atom, '^[a-f]*$')
        
    def test_custom_key_with_seed(self):
        # Generate custom key with 3 atoms, '-' separator, min length 3, max length 4, uppercase letters, and seed value 42
        key = generate(num_of_atom=3, separator='-', min_atom_len=3, max_atom_len=4, type_of_value='char', capital='all', seed=42).get_key()
        self.assertIsInstance(key, str)
        self.assertEqual(key.count('-'), 2)
        atoms = key.split('-')
        for atom in atoms:
            self.assertGreaterEqual(len(atom), 3)
            self.assertLessEqual(len(atom), 4)
            self.assertRegex(atom, '^[A-F]*$')
        
    def test_custom_key_with_extras(self):
        # Generate custom key with 2 atoms, ':' separator, min length 3, max length 3, lowercase letters, and additional characters
        extras = ['%', '&', '#']
        key = generate(num_of_atom=2, separator=':', min_atom_len=3, max_atom_len=3, type_of_value='char', capital='none', extras=extras).get_key()
        self.assertIsInstance(key, str)
        self.assertEqual(key.count(':'), 1)
        atoms = key.split(':')
        for atom in atoms:
            self.assertGreaterEqual(len(atom), 3)
            self.assertLessEqual(len(atom), 3)
            self.assertRegex(atom, '^[a-f%&#]*$')
        
if __name__ == '__main__':
    unittest.main()
