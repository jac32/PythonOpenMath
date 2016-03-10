
""" Parsing Unit Tests
======================

Test cases for the parsing of OpenMath XML Strings
"""
import unittest
import CDs
from CDs import *
from symbol import Symbol
from fractions import Fraction
from openmath import parse_om_file, om_string, om_pretty_print,evaluate_om_string
from CDs.arith1 import *


################################################################
#
#Class for decoding OpenMath XML into 
#
class Decoding(unittest.TestCase):
    """ Testing of Decoding/Parsing Methods"""

    def test_decode_bool_true(self):
        print('Decoding:test_bool_true')
        self.assertTrue(parse_om_file('tst/true.xml'))
        
    def test_decode_bool_false(self):
        print('Decoding:test_bool_false')
        self.assertTrue(not parse_om_file('tst/false.xml'))

    def test_decode_int_42(self):
        print('Decoding:test_int_42')
        self.assertEqual(42, parse_om_file('tst/integer.xml'))

    def test_decode_list_simple(self):
        print('Decoding:test_list_simple')
        test_list = [41, True, 43]
        self.assertListEqual(test_list, parse_om_file('tst/list.xml'))

    def test_decode_list_nested(self):
        print('Decoding:test_list_nested')
        test_list = [1, 2, [3, 4, 5]]
        self.assertListEqual(test_list, parse_om_file('tst/listnested.xml'))

    def test_decode_rational_list_1_2(self):
        print('Decoding:test_rational_1_2')
        test_rational = [1, Fraction(1,2)]
        self.assertEqual(test_rational, parse_om_file('tst/rational.xml'))

    def test_decode_complex_simp(self):
        print('Decoding:test_complex_1_2')
        test_complex = 2 + 3j
        self.assertEqual(test_complex, parse_om_file('tst/complexsimp.xml'))

    def test_decode_complex_ratios(self):
        print('Decoding:test_complex_ratios')
        test_complex = Fraction(2,3) + Fraction(5,4) * 1j
        self.assertEqual(test_complex, parse_om_file('tst/complex.xml'))

    def test_decode_range_neg_to_pos_10(self):
        print('Decoding:test_range_neg_to_pos_10')
        test_range = range(-10,10)
        self.assertEqual(test_range, parse_om_file('tst/range.xml'))

    def test_decode_float_list(self):
        print('Decoding:test_float_list')
        test_float_list = [0, 1.0, 0.5, -1, 19487171.0, 5.1315811823070673e-08, -19487171.0, -5.1315811823070673e-08]
        self.assertListEqual(test_float_list, parse_om_file('tst/float.xml'))

    def test_decode_factorial(self):
        print('Decoding:test_factorial')
        test_factorial = CDs.factorial.Factorial(10)
        self.assertEqual(test_factorial.args, parse_om_file('tst/factorial.xml').args)

    def test_decode_matrix_3x3(self):
        print('Decoding:test_matrix_3x3')
        test_matrix = CDs.matrix.Matrix(CDs.matrix.MatrixRow(1,2,3),
                              CDs.matrix.MatrixRow(42, 5, 6),
                              CDs.matrix.MatrixRow(0, -1, -100))
        
        self.assertListEqual(test_matrix.flatten(),
                            parse_om_file('tst/matrix.xml').flatten())

    def test_eval_plus(self):
        print('Decoding:test_plus')
        test_plus = 27
        self.assertEqual(test_plus, parse_om_file('tst/plus.xml').eval())
        
    def test_eval_minus(self):
        print('Decoding:test_minus')
        test_minus = 5
        self.assertEqual(test_minus, parse_om_file('tst/minus.xml').eval())
        
    def test_eval_times(self):
        print('Decoding:test_times')
        test_times = 5
        self.assertEqual(test_times , parse_om_file('tst/times.xml').eval())
        
    def test_eval_divide(self):
        print('Decoding:test_divide')
        test_div = 200.0
        self.assertEqual(test_div , parse_om_file('tst/divide.xml').eval())
      
    def test_eval_power(self):
        print('Decoding:test_power')
        test_pow = 16
        self.assertEqual(test_pow , parse_om_file('tst/power.xml').eval())
    
    def test_eval_root(self):
        print('Decoding:test_power')
        test_root = 2
        self.assertEqual(test_root, parse_om_file('tst/root.xml').eval())
          
    def test_eval_abs(self):
        print('Decoding:test_abs')
        test_abs = 15
        self.assertEqual(test_abs , parse_om_file('tst/abs.xml').eval())
        
    def test_eval_nested_plus(self):
        print('Decoding:test_divide')
        test_plus = 22
        self.assertEqual(test_plus, parse_om_file('tst/nestedplus.xml').eval())
        
    def test_eval_gcd(self):
        print('Decoding:test_gcd')
        test_plus = 3
        self.assertEqual(test_plus, parse_om_file('tst/gcd.xml').eval())
        
    def test_eval_lcm(self):
        print('Decoding:test_lcm')
        test_plus = 36
        self.assertEqual(test_plus, parse_om_file('tst/lcm.xml').eval())
        
    def test_eval_unary_minus(self):
        print('Decoding:test_unary_minus')
        test_plus = -8
        self.assertEqual(test_plus, parse_om_file('tst/unminus.xml').eval()) 


#################################################################################
#
# class for encoding objects into OpenMath XML
#
class Encoding(unittest.TestCase):
    """ Testing of Decoding/Parsing Methods"""

    def test_encode_int_42(self):
        print('Encoding:test_encode_int_42')
        self.assertEqual(om_string(parse_om_file('tst/integer.xml')),
                         om_string(42))

    def test_encode_plus(self):
        print('Encoding:test_encode_plus')
        self.assertEqual(om_string(parse_om_file('tst/plus.xml')),
                         om_string(Arith1Plus(15, 10, 2)))

    def test_encode_minus(self):
        print('Encoding:test_encode_minus')
        self.assertEqual(om_string(parse_om_file('tst/minus.xml')),
                         om_string(Arith1Minus(15, 10)))

    def test_encode_times(self):
        print('Encoding:test_encode_times')
        self.assertEqual(om_string(parse_om_file('tst/times.xml')),
                         om_string(Arith1Times(5, 1)))


    def test_encode_divide(self):
        print('Encoding:test_encode_divide')
        self.assertEqual(om_string(parse_om_file('tst/divide.xml')),
                         om_string(Arith1Divide(200, 1)))       


    def test_encode_nested_plus(self):
        print('Encoding:test_encode_nested_plus')
        self.assertEqual(om_string(parse_om_file('tst/nestedplus.xml')),
                         om_string(Arith1Plus(10, Arith1Times(3,4))))       


    def test_encode_factorial(self):
        print('Encoding:test_encode_plus')

        Factorial = CDs.factorial.Factorial
        
        self.assertEqual(om_string(parse_om_file('tst/factorial.xml')),
                         om_string(Factorial(10)))

    def test_encode_dictionary(self):
        print('Encoding:test_encode_dict')

        Dictionary = CDs.dictionary.Dictionary
        KeyValuePair = CDs.dictionary.KeyValuePair        

        self.assertEqual(om_string(parse_om_file('tst/dict.xml')),
                         om_string(Dictionary(KeyValuePair('key1',1),KeyValuePair('key2',2),KeyValuePair('key3',3))))

    def test_encode_ome(self):
        print('Encoding:test_encode_ome')
        self.assertEqual('<OMOBJ><OME><OMS cd="arith_error" name="divide_by_zero" /><OMS cd="arith1" name="divide" /></OME></OMOBJ>',
                         evaluate_om_string(open("tst/dividebyzero.xml","r").read()))


    def test_encode_matrix(self):
        print('Encoding:test_encode_matrix')

        Matrix = CDs.matrix.Matrix
        MatrixRow = CDs.matrix.MatrixRow

        self.assertEqual(om_string(parse_om_file('tst/matrix.xml')),
                        om_string(Matrix(MatrixRow(1, 2, 3),
                                         MatrixRow(42, 5, 6),
                                         MatrixRow(0, -1, -100))))


if __name__ == '__main__':
     unittest.main()
