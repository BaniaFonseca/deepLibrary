from django.shortcuts import render
from django.views import View

class DeepShelf(View):
 
    def get(self, request):
        pass
        # book = self.crud.get_one(Book, {'year': 2020})
        # demo = book
        # demos = [demo for _ in range(6)]
        # request.session['current'] = {}
        # return render(request, 'deepshelf/deepshelf.html',
        #     context={'edocuments': demos}, content_type='text/html')