from core.storage import crudabc
from core.storage.connection import Connection

class OSCRUD(crudabc.OSCRUD):
    """ Object Storage CRUD Class"""
    def __init__(self):
        super().__init__()
        self.connection = Connection.get_connection()
    
    @property
    def connection(self):
        return self.__connection

    @connection.setter
    def connection(self, value):
        self.__connection = value
    
    def get_object(self, bucketname, objectname):
        return self.connection.get_object(bucketname, objectname)
    
    def save_object(self, bucketname, objectname, data, length, contenttype):
        self.connection.put_object(
            bucketname, 
            objectname,
            data,
            length,
            contenttype)

# filename = dirname(abspath(__file__))
#             with open(join(filename,'pdf/demo.pdf'), 'rb') as pdf:
#                 pdfr = PyPDF2.PdfFileReader(pdf) 
#                 npages = pdfr.numPages
#                 for j in range(npages):
#                     page = pdfr.getPage(j)
#                     pdw = PyPDF2.PdfFileWriter()
#                     pdw.addPage(page)
#                     pdfbinarydata = io.BytesIO()
#                     pdw.write(pdfbinarydata)
#                     nbytes = pdfbinarydata.tell()
#                     pdfbinarydata.seek(0)
#                     self.oscrud.save_object(
#                         type, id+str(j+1), 
#                         pdfbinarydata, 
#                         nbytes,
#                         contenttype='application/pdf')