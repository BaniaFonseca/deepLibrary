from django.shortcuts import render
from django.http import JsonResponse
import PyPDF2
import io
from base64 import b64encode
from django.http import HttpResponse

from os.path import abspath, dirname, join

from core.view import ViewABC
from core.storage.crud import CRUD

class LightWeightViewer(ViewABC):

    def get(self, request):
        type = request.GET.get('type')
        id = request.GET.get('id')
        pages = request.GET.get('pages')

        print(" ++++ pages {}".format(pages))
        return render(request, 'lwviewer/lwviewer.html',
            context={'type' : type, 'id': id, 'pages' : pages}, 
            content_type='text/html')

class LightWeightPDFLoader(ViewABC):

    def __init__(self):
        super().__init__()
        self.oscrud = CRUD()
            
    def get(self, request):    
        page = request.GET.get('page')
        type = request.GET.get('type')
        id = request.GET.get('id')
        
        print(" --- id {} type {} page {}".format(id, type, page))
        # data  = None
        
        if False:
            filename = dirname(abspath(__file__))
            with open(join(filename,'pdf/demo.pdf'), 'rb') as pdf:
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
                    self.oscrud.save_object(
                        type, id+str(j+1), 
                        pdfbinarydata, 
                        nbytes,
                        contenttype='application/pdf')
        try:
            self.oscrud = CRUD()
            response = self.oscrud.get_object(type, id+page)
            return HttpResponse(response)
        finally:
            response.close()
            response.release_conn()