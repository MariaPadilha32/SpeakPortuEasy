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
            return redirect('success')
        else:
            print('error')
            for field, errors in form.errors.items():
                print(f"Field '{field}' errors: {errors}")
    return render(request, 'registration/register.html', {'form': form})


def success(request):
    return render(request, 'registration/success.html')
