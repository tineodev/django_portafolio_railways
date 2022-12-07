from django.shortcuts import render

# Create your views here.
from django.views.generic import View

class Index(View):
    def get(self, request):
        template_name = 'portfolio/index2.html'
        return render(request, template_name)