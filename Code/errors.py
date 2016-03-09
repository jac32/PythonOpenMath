class UnsupportedCDError(Exception):
    def __init__(self, cd, name):
       self.cd   = cd
       self.name = name
       self.obj  = build()

    def __str__(self):
        return ET.tostring(self.obj)

    def build(self):
        omobj = Element('OMOBJ')
        ome   = Element('OME')
        oms1  = Element('OMS')
        
        oms1.attrib = {'cd' : 'error',
                       'name' : 'unsupported_CD'}
        
        oms2  = Element('OMS')
        oms2.attrib = {'cd' : self.cd,
                       'name' : self.name}

        omobj.insert(1, ome)
        ome.insert(1, oms1)
        ome.insert(2, oms2)

        return omobj
