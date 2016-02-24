import openmath
from openmath import *

s = '<OMOBJ> <OMI>42</OMI> </OMOBJ>'
ParseOMstring(s)

s = '<OMOBJ> <OMA> <OMS cd="list1" name="list"/> <OMI>41</OMI> <OMI>42</OMI> <OMI>43</OMI> </OMA> </OMOBJ>'
ParseOMstring(s)

s = '<OMOBJ> <OMA> <OMS cd="list1" name="list"/> <OMI>41</OMI> <OMI>42</OMI> <OMI>43</OMI> <OMA> <OMS cd="list1" name="list"/> <OMI>41</OMI> <OMI>42</OMI> <OMI>43</OMI> </OMA> </OMA> </OMOBJ>'
ParseOMstring(s)

s= '<OMOBJ> <OMA> <OMS cd="logic1" name="false"/> </OMA> </OMOBJ>'
ParseOMstring(s)


ParseOMfile('tst/integer.xml')
ParseOMfile('tst/list.xml')
ParseOMfile('tst/listnested.xml')
ParseOMfile('tst/bool.xml')
ParseOMfile('tst/rational.xml')
ParseOMfile('tst/complex_simp.xml')
ParseOMfile('tst/range.xml')
ParseOMfile('tst/matrix.xml')
OMprint(ParseOMfile('tst/matrix.xml'))

OMprint(range(-20,20))
OMprint(ParseOMstring('<OMOBJ><OMA><OMS cd="interval1" name="integer_interval" /><OMI>-20</OMI><OMI>20</OMI></OMA></OMOBJ>'))




print
OMprint(1+2j)
OMprint((3,2))
OMprint(False)
OMstring(42)
OMprint(42)

OMstring([1,2,3])
OMprint([1,2,3])

OMprint([1,2,[3,4,5]])
OMstring([1,2,[3,4,5]])

# tests
a = 42
a == ParseOMstring(OMstring(a))

a = [1,2,3]
a == ParseOMstring(OMstring(a))

a = [1,2,[3,4,5]]
a == ParseOMstring(OMstring(a))


