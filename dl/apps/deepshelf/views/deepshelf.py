from django.shortcuts import render

from apps.deepshelf.models.edocument import Book
from apps.core.view import ViewABC


class DeepShelf(ViewABC):
 
    def get(self, request):
                
        book = self.crud.get_one(Book, {'year': 2018})
        demo = book
        demos = [demo for _ in range(6)]
        
        return render(request, 'deepshelf/deepshelf.html',
            context={'edocuments': demos}, content_type='text/html')