import PyPDF2
import io
from os.path import abspath, dirname, join

from core.storage.oscrud import OSCRUD

oscrud = OSCRUD()


def get_page(id):
    filename = dirname(abspath(__file__))
    with open(join(filename, id), 'rb') as pdf:
        pdfr = PyPDF2.PdfFileReader(pdf)
        pdfpage = pdfr.getPage(0)
        pdw = PyPDF2.PdfFileWriter()
        pdw.addPage(pdfpage)
        pdfbinarydata = io.BytesIO()
        pdw.write(pdfbinarydata)
        pdfbinarydata.seek(0)
        
        return pdfbinarydata.read()
            

             


def splitpdf():
    filename = dirname(abspath(__file__))
    id = "5f390b30ea0e67ac51555b32"
    with open(join(filename,'demo.pdf'), 'rb') as pdf:
        pdfr = PyPDF2.PdfFileReader(pdf) 
        npages = pdfr.numPages
        for j in range(npages):
            page = pdfr.getPage(j)
            pdw = PyPDF2.PdfFileWriter()
            pdw.addPage(page)
            pdfbinarydata = io.BytesIO()
            pdw.write(pdfbinarydata)
            nbytes = pdfbinarydata.tell()
            pdfbinarydata.seek(0)
            with open(id+str(j+1), 'wb') as out:
                out.write(pdfbinarydata.read())

            
def demo():
    filename = dirname(abspath(__file__))
    id = "5f390b30ea0e67ac51555b32"
    with open(join(filename,'demo.pdf'), 'rb') as pdf:
        pdfr = PyPDF2.PdfFileReader(pdf) 
        npages = pdfr.numPages
        for j in range(npages):
            page = pdfr.getPage(j)
            pdw = PyPDF2.PdfFileWriter()
            pdw.addPage(page)
            pdfbinarydata = io.BytesIO()
            pdw.write(pdfbinarydata)
            nbytes = pdfbinarydata.tell()
            pdfbinarydata.seek(0)
            oscrud.save_object(
                'books', id+str(j+1), 
                pdfbinarydata, 
                nbytes,
                contenttype='application/pdf')