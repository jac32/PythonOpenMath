from openmath import *
from fractions import Fraction


s = '<OMOBJ> <OMI>42</OMI> </OMOBJ>'
parse_om_string(s)

s = '<OMOBJ> <OMA> <OMS cd="list1" name="list"/> <OMI>41</OMI> <OMI>42</OMI> <OMI>43</OMI> </OMA> </OMOBJ>'
parse_om_string(s)

s = '<OMOBJ> <OMA> <OMS cd="list1" name="list"/> <OMI>41</OMI> <OMI>42</OMI> <OMI>43</OMI> <OMA> <OMS cd="list1" name="list"/> <OMI>41</OMI> <OMI>42</OMI> <OMI>43</OMI> </OMA> </OMA> </OMOBJ>'
parse_om_string(s)

s= '<OMOBJ> <OMA> <OMS cd="logic1" name="false"/> </OMA> </OMOBJ>'
parse_om_string(s)

a = '<OMOBJ> <OMF dec=\"2.3\"></OMF> </OMOBJ>'
parse_om_string(a)


parse_om_file('tst/integer.xml')
parse_om_file('tst/list.xml')
parse_om_file('tst/listnested.xml')
parse_om_file('tst/bool.xml')
parse_om_file('tst/rational.xml')
parse_om_file('tst/complex_simp.xml')
parse_om_file('tst/range.xml')
parse_om_file('tst/float.xml')
#parse_om_file('tst/factorial.xml')
a= parse_om_file('tst/matrix.xml')
om_print(a)

om_print(range(-20,20))
om_print(parse_om_string('<OMOBJ><OMA><OMS cd="interval1" name="integer_interval" /><OMI>-20</OMI><OMI>20</OMI></OMA></OMOBJ>'))


om_print(1+2j)
om_print(Fraction(3,2))
om_print(False)

om_string([1,2,3])
om_print([1,2,3])

om_print([1,2,[3,4,5]])
om_string([1,2,[3,4,5]])

# tests
a = 42
a == parse_om_string(om_string(a))


a = 5.4
a == parse_om_string(om_string(a))

a = [1,2,3]
a == parse_om_string(om_string(a))

a = [1,2,[3,4,5]]
a == parse_om_string(om_string(a))


