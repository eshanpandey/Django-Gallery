from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from .forms import ImageUploadForm
from .models import Image
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        # Use CustomUserCreationForm instead of UserCreationForm
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('gallery')
    else:
        # Use CustomUserCreationForm instead of UserCreationForm
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('gallery')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user 
            image.save()
            return redirect('gallery') 
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

@login_required
def gallery(request):
    images = Image.objects.filter(user=request.user)
    return render(request, 'gallery.html', {'images': images})
def home(request):
    return render(request, 'home.html')
