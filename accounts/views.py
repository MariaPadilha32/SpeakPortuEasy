from django.shortcuts import render, redirect
from .admin import CustomUserCreationForm
from django.contrib import messages


# Create your views here.
def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_valid = False
            user.save()
            return redirect('home')
        else:
            print('erorr')
    return render(request, 'registration/register.html', {'form': form})


def recover_password(request):
    return render(request, 'registration/recover-password.html')