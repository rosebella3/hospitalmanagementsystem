from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class CustomAuth(AuthenticationForm):
    ## add css classes

    def __init__(self, args, kwargs):
        super(CustomAuth, self).__init__(args, kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-user'

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

