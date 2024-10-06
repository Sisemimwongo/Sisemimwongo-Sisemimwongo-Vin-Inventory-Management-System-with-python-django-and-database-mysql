from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created for {username}. Continue to login')
            # Redirect to dashboard after successful registration
            return redirect('user-login')
    else:
        form = CreateUserForm()
    context = {
        'form': form,
    }
    return render(request, 'user/register.html', context)

def profile(request):
    return render(request, 'user/profile.html')

def profile_update(request):
    if request.method== 'POST':
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
    else:
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'profile_form': profile_form
    }
    return render(request, 'user/profile_update.html', context)
