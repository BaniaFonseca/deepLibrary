from django.shortcuts import render

from apps.deepshelf.models.edocument import Book
from core.view import ViewABC


class DeepShelf(ViewABC):
 
    def get(self, request):
        book = self.crud.get_one(Book, {'year': 2020})
        demo = book
        demos = [demo for _ in range(6)]
        doc = demo.as_document()
        doc['_id'] = str(doc['_id'])
        request.session['demo'] = doc
        return render(request, 'deepshelf/deepshelf.html',
            context={'edocuments': demos}, content_type='text/html')