from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm



class CadastroUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',
                  'password1',
                  'password2']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username',
                  'password']


class CustomLogin(AuthenticationForm): # Para fazer o login, iremos utilizar uma classe que irá herdar do AuthenticationForm.
                                       # É necessario importar o AuthenticationForm.
    class Meta:
        fields = ['username','password']