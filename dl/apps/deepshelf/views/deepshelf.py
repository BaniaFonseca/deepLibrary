from apps.core.views.core import *

from apps.deepshelf.models.electronicdocument import ElectronicDocument as edoc

class DeepShelf(View):

    def __init__(self):   
        super().__init__()
    
    def get(self, request):
        demo = edoc()
        demos = [demo for _ in range(6)]
        return render(request, 'deepshelf/deepshelf.html',
            context={'edocuments': demos}, content_type='text/html')