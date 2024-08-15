from django import forms
import _sweetsaratov_.widgets as widgets
from . import models


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ('username', 'password', 'email' )

        labels = {
            'username': 'Имя пользователя',
            'password': 'Пароль',
            'email': 'Электронная почта'
        }
        widgets = {
            'password': forms.PasswordInput(),
            'email': forms.EmailInput()
        }
        # widgets = {
        #     "date_of_birth": widgets.DateInput(
        #         format='%d/%m/%Y',
        #         attrs={
        #             'class':        'form-control',
        #             'placeholder':  'Выберите дату',
        #             'type':         'date'
        #         }
        #     )
        # }


class LoginForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ('username', 'password')

        labels = {
            'username': 'Имя пользователя',
            'password': 'Пароль'
        }


class NewMessageForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ('username', 'message' )

        labels = {
            'username': 'Имя пользователя',
            'message': 'Сообщение'
        }
        widgets = {
            'password': forms.PasswordInput(),
            'email': forms.EmailInput()
        }