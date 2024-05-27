from .models import User
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, RadioSelect


class UserForm(ModelForm):

  class Meta:
    model = User
    fields = ['name', 'surname', 'password', 'email', 'age', 'gender']

    widgets = {
      'name': TextInput(attrs={
        "type": "text",
        "name": "name",
        "placeholder": "Имя",
        "id": "name",
        "pattern": "[А-ЯЁA-Z][а-яёa-z]+"
      }),
      'surname': TextInput(attrs={
        "type": "text",
        "name": "surname",
        "placeholder": "Фамилия",
        "id": "surname",
        "pattern": "[А-ЯЁA-Z][а-яёa-z]+"
      }),
      'password': PasswordInput(attrs={
        "type": "password",
        "name": "pass",
        "placeholder": "Пароль",
        "id": "pass",
        "minlength": "6"
      }),
      'email': TextInput(attrs={
        "type": "email",
        "name": "email",
        "placeholder": "Email",
        "id": "email"
      }),
      'age': TextInput(attrs={
        "type": "number",
        "name": "age",
        "placeholder": "Возраст",
        "id": "age",
        "min": "12",
        "max": "150"
      }),
      'gender': RadioSelect(attrs={
        "id": "gender"    
      })
    }