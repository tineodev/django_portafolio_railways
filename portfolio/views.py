from django.shortcuts import render, redirect

from django.views.generic import View, CreateView
from .forms import NewUser

# Create your views here.

class Index(View):
    def get(self, request):
        template_name = 'portfolio/index2.html'
        return render(request, template_name)


class SignUp(CreateView):
    form_class = NewUser
    template_name = 'registration/register.html'

    def form_valid(self, form):
        form.save()
        return redirect('login')


class Main(View):
    def get(self, request):
        return render()