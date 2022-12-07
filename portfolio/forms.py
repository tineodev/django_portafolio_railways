from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUser(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(NewUser, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user


class Project_form(forms.Form):
    titulo = forms.CharField(max_length=100, required=False)
    descripcion = forms.CharField(max_length=200, required=False)
    foto_url = forms.URLField(required=False)
    #!editar tags = forms.CharField(max_length=100, required=False)
    github_url = forms.URLField(required=False)
