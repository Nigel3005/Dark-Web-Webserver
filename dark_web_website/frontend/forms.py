from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=50)
    # password = forms.CharField(label='Password', max_length=50)
    #
    # class Meta:
    #     model = User
    #     fields = ('username', 'password')
    #
    # def __init__(self, *args, **kwargs):
    #     super(LoginForm, self).__init__(*args, **kwargs)
