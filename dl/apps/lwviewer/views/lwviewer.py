from django.shortcuts import render
from django.http import JsonResponse
import PyPDF2
import io
from base64 import b64encode

from os.path import abspath, dirname, join

from core.view import ViewABC

class LightWeightViewer(ViewABC):

    def get(self, request):

        greetings = "Hi, Keep Calm the LightWeightViewer is being built"
        return render(request, 'lwviewer/lwviewer.html',
            context={'greetings' : greetings, 'demo': request.session['demo']}, 
            content_type='text/html')

class LightWeightPDFLoader(ViewABC):

    def get(self, request):    
        page = request.GET.get('edocpage')
        type = request.GET.get('edoctype')
        id = request.GET.get('edocid')
        data  = None
        filename = dirname(abspath(__file__))
        with open(join(filename,'pdf/demo.pdf'), 'rb') as pdf:
            ENCODING = 'utf-8'
            pdfr = PyPDF2.PdfFileReader(pdf) 
            npages = pdfr.numPages
            page = pdfr.getPage(int(page)-1)
            pdw = PyPDF2.PdfFileWriter()
            pdw.addPage(page)
            pdfbinarydata = io.BytesIO()
            pdw.write(pdfbinarydata)
            base64_bytes = b64encode(pdfbinarydata.getvalue())
            pdfbase64data = base64_bytes.decode(ENCODING)
            data  = {'pdfbase64data' : pdfbase64data}
        return JsonResponse(data)
