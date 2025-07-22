from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return HttpResponse("Welcome! Go to /register or /login.")

# Registration View
def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'accounts/register.html', {'form': form})

# Secret Page (only for logged-in users)
@login_required
def secret_page(request):
     if request.method == 'POST':
        q1 = request.POST.get('q1')
        q2 = request.POST.get('q2')
        q3 = request.POST.get('q3')
        print(f"User answers: Q1={q1}, Q2={q2}, Q3={q3}")
        return HttpResponse(f"Thanks for your answers, {request.user.username}! 👍")

     return render(request, 'accounts/secret.html')
