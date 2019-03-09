from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm

""" class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
 """

def SignUp(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('login')
    else:
        f = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': f})    