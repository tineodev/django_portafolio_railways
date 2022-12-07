from django.shortcuts import render, redirect

from django.views.generic import View, CreateView
from .forms import NewUser

from django.views.generic import FormView
from .models import Project_model
from .forms import Project_form
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


class Main_page(View):
    def get(self, request):
        template_name='portfolio/main.html'
        extra_context ={
            'lista': Project_model.objects.all()
        }
        return render(request, template_name, extra_context)


class CreateProject(FormView):
    model = Project_model
    form_class = Project_form
    template_name = 'portfolio/project.html'

    def form_valid(self, form):
        Project_model.objects.create(**form.cleaned_data)
        return redirect('main')
