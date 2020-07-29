from apps.core.views.core import *

class Home(DeepLibraryBaseView):
    
    def __init__(self):
        super().__init__()

    def get(self, request):
        return render(request, 'home/index.html',content_type='text/html')