import PyPDF2
import io
import binascii

with open('demo.0.pdf', 'rb') as pdf:
    pdfr = PyPDF2.PdfFileReader(pdf) 
    npages = pdfr.numPages
    # print("number of pages {}".format(pfr.numPages))
    page = pdfr.getPage(0)
    pdw = PyPDF2.PdfFileWriter()
    pdw.addPage(page)
    file = io.BytesIO()
    pdw.write(file)
    
    print(binascii.b2a_base64(file.getvalue(), newline=False))

    # print(file.getvalue())    
    # with open('temp.pdf', 'wb') as temp:
    #     temp.write(file.getvalue())
            
    # for i in range(npages):
    #     pdw = PyPDF2.PdfFileWriter()
    #     pdw.addPage(pdfr.getPage(i))
    #     with open('demo.{}.pdf'.format(i), 'wb') as file:
    #         pdw.write(file)