from django.shortcuts import render, redirect

from django.views.generic import View, CreateView
from .forms import NewUser

from django.views.generic import FormView
from .models import Project_model, IPs_model
from .forms import Project_form

from django.contrib.auth.mixins import LoginRequiredMixin

from ipware import get_client_ip
# Create your views here.

class paginas(View):
    def get(self, request):
        template_name = 'portfolio/paginas.html'
        return render(request, template_name)

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


class Main_page(LoginRequiredMixin,View):
    def get(self, request):
        template_name='portfolio/main.html'
        extra_context ={
            'lista': Project_model.objects.all()
        }

        ip_user, ip_boolean = get_client_ip(request)
        res = IPs_model(ip = ip_user)
        res.save()
        return render(request, template_name, extra_context)


class CreateProject(LoginRequiredMixin,FormView):
    model = Project_model
    form_class = Project_form
    template_name = 'portfolio/project.html'

    def form_valid(self, form):
        Project_model.objects.create(**form.cleaned_data)
        return redirect('main')


class DeleteDB(View):
    def get(self,request):
        Project_model.objects.get(id=19).delete()
        return redirect('paginas')