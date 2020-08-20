from django.shortcuts import render

from core.view import ViewABC

class LightWeightViewer(ViewABC):

    def get(self, request):

        greetings = "Hi, Keep Calm the LightWeightViewer is being built"
        return render(request, 'lwviewer/lwviewer.html',
            context={'greetings' : greetings, 'demo': request.session['demo']}, 
            content_type='text/html')