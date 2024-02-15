from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms
from .models import Image

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'password1', 'password2')
