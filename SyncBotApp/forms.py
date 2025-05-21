from .models import CustomUser
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class loginUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', "password")
        widgets = {
            'password': forms.PasswordInput(),
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username'}),
        }
        labels = {
            'username': _('username'),
            'password': _('Password'),
        }

    
    def __init__(self, *args, **kwargs):
        super(loginUserForm, self).__init__(*args, **kwargs)
        common_classes = (
            'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg '
            'focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 '
            'dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 '
            'dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
        )
        
        for field_name, field in self.fields.items():
            existing_classes = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f'{existing_classes} {common_classes}'.strip()


class CreateNewUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', "password1", "password2", "email", "first_name", "last_name")
        widgets = {
            'password1': forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}),
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name'}),
        }
        labels = {
            'username': _('username'),
            'password1': _('Password'),
            'password2': _('Confirm Password'),
            'email': _('Email'),
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
        }

    
    def __init__(self, *args, **kwargs):
        super(CreateNewUserForm, self).__init__(*args, **kwargs)
        common_classes = (
            'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg '
            'focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 '
            'dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 '
            'dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
        )
        
        for field_name, field in self.fields.items():
            existing_classes = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f'{existing_classes} {common_classes}'.strip()

            # Optionally set placeholders for password fields
            if field_name == 'password1':
                field.widget.attrs['placeholder'] = 'Enter your password'
            elif field_name == 'password2':
                field.widget.attrs['placeholder'] = 'Confirm your password'
