""" Parsing Unit Tests
======================

Test cases for the parsing of OpenMath XML Strings
"""

import unittest
from fractions import Fraction
from factorial import Factorial
from matrix import Matrix, MatrixRow
from openmath import parse_om_file, om_string


class Decoding(unittest.TestCase):
    """ Testing of Decoding/Parsing Methods"""

    def test_encode_bool_true(self):
        print('Decoding:test_bool_true')
        self.assertTrue(parse_om_file('tst/true.xml'))
        
    def test_encode_bool_false(self):
        print('Decoding:test_bool_false')
        self.assertTrue(not parse_om_file('tst/false.xml'))

    def test_encode_int_42(self):
        print('Decoding:test_int_42')
        self.assertEqual(42, parse_om_file('tst/integer.xml'))

    def test_encode_list_simple(self):
        print('Decoding:test_list_simple')
        test_list = [41, True, 43]
        self.assertListEqual(test_list, parse_om_file('tst/list.xml'))

    def test_encode_list_nested(self):
        print('Decoding:test_list_nested')
        test_list = [1, 2, [3, 4, 5]]
        self.assertListEqual(test_list, parse_om_file('tst/listnested.xml'))

    def test_encode_rational_list_1_2(self):
        print('Decoding:test_rational_1_2')
        test_rational = [1, Fraction(1,2)]
        self.assertEqual(test_rational, parse_om_file('tst/rational.xml'))

    def test_encode_complex_simp(self):
        print('Decoding:test_complex_1_2')
        test_complex = 2 + 3j
        self.assertEqual(test_complex, parse_om_file('tst/complexsimp.xml'))

    def test_encode_complex_ratios(self):
        print('Decoding:test_complex_ratios')
        test_complex = Fraction(2,3) + Fraction(5,4) * 1j
        self.assertEqual(test_complex, parse_om_file('tst/complex.xml'))

    def test_encode_range_neg_to_pos_10(self):
        print('Decoding:test_range_neg_to_pos_10')
        test_range = range(-10,10)
        self.assertEqual(test_range, parse_om_file('tst/range.xml'))

    def test_encode_float_list(self):
        print('Decoding:test_float_list')
        test_float_list = [0, 1.0, 0.5, -1, 19487171.0, 5.1315811823070673e-08, -19487171.0, -5.1315811823070673e-08]
        self.assertListEqual(test_float_list, parse_om_file('tst/float.xml'))

    def test_encode_factorial(self):
        print('Decoding:test_factorial')
        test_factorial = Factorial(10)
        self.assertEqual(test_factorial.num, parse_om_file('tst/Factorial.xml').num)

    def test_encode_matrix_3x3(self):
        print('Decoding:test_matrix_3x3')
        test_matrix = Matrix(MatrixRow(1,2,3),
                              MatrixRow(42, 5, 6),
                              MatrixRow(0, -1, -100))
        
        self.assertListEqual(test_matrix.flatten(),
                            parse_om_file('tst/Matrix.xml').flatten())


class Decoding(unittest.TestCase):
    """ Testing of Decoding/Parsing Methods"""

    def test_decode_int_42(self):
        print('Encoding:test_decode_int_42')
        test_result = '<OMOBJ> <OMI>42</OMI> </OMOBJ>'
        self.assertEqual(test_result, om_string(42))

if __name__ == '__main__':
    unittest.main()
