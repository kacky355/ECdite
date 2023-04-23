from django import forms
from .models import MyUser
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import AuthenticationForm

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label='name')
    date_of_birth = forms.DateField(label='生年月日')
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='パスワード')
    
    class Meta():
        model = MyUser
        fields =['username','date_of_birth','email','password']
    
    def save(self, commit=False):
        user = super().save(commit=False)
        validate_password(self.cleaned_data['password'],user)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user
    


class LoginForm(AuthenticationForm):
    email = forms.EmailField(label='Email address')
    password = forms.CharField(label='password', widget=forms.PasswordInput())
    remenber = forms.BooleanField(label='keep login', required=False)

# もう一つのログイン実装
# class LoginForm(forms.Form):
#     email = forms.EmailField(label='Email address')
#     password = forms.CharField(label='password', widget=forms.PasswordInput())