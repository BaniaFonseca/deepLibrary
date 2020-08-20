import PyPDF2

with open('demo.pdf', 'rb') as pdf:
    pdfr = PyPDF2.PdfFileReader(pdf) 
    npages = pdfr.numPages
    # print("number of pages {}".format(pfr.numPages))
    # page = pdfr.getPage(1)
    # print(page.extractText())

    for i in range(npages):
        pdw = PyPDF2.PdfFileWriter()
        pdw.addPage(pdfr.getPage(i))
        with open('demo.{}.pdf'.format(i), 'wb') as file:
            pdw.write(file)