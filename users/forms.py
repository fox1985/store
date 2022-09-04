from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from users.models import User

class UserLoginForm(AuthenticationForm):
    """Форма авторизации"""
    username = forms.CharField(widget=forms.TextInput(attrs={"class": 'form-control py-4', "placeholder" : 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": 'form-control py-4', "placeholder" : 'Введите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    """Форма регистрации"""
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": 'form-control py-4', "placeholder" : 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": 'form-control py-4', "placeholder" : 'Введите фамилию'}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class": 'form-control py-4', "placeholder" : 'Введите имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"class": 'form-control py-4', "placeholder" : 'Введите адрес эл. почты'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": 'form-control py-4', "placeholder" : 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": 'form-control py-4', "placeholder" : 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2' )


class UserProfileForm(UserChangeForm):
    """Форма Провиля"""
    username = forms.CharField(widget=forms.TextInput({'readonly': True}))
    email = forms.CharField(widget=forms.EmailInput({'readonly': True}))
    image = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',  'image')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for fileld_name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'
