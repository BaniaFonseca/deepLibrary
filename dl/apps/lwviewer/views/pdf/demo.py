import PyPDF2
import io

with open('demo.pdf', 'rb') as pdf:
    pdfr = PyPDF2.PdfFileReader(pdf) 
    npages = pdfr.numPages

    print(npages)            
    for i in range(npages):
        pdw = PyPDF2.PdfFileWriter()
        pdw.addPage(pdfr.getPage(i))
        with open('demo.{}.pdf'.format(i+1), 'wb') as file:
            pdw.write(file)