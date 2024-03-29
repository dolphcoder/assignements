from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.messages.views import SuccessMessageMixin
# from django.contrib.auth.mixins import  LoginRequiredMixin
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages



class RegisterView(SuccessMessageMixin, CreateView):
    template_name = 'accounts/register.html'
    form_class = UserRegisterForm
    success_url = '/accounts/login/'
    success_message = 'Successfully created user!'

# Create your views here.
# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('home')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'accounts/register.html', {'form': form})
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Successfully Updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        return render(request, 'accounts/profile.html', context)