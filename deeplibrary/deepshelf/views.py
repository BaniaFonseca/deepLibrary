from django.views import View
from django.http import HttpResponse

class DeepShelf(View):

    def get(self, request):
        # < logic here >
        return HttpResponse("Hi I am DeepShelf!")
   