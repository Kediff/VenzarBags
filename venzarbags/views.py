from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.
def landing(request):
    return render(request, 'landing.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
      
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return HttpResponse("Login successful")
        else:
            return HttpResponse("Invalid credentials", status=401)
    else:
        return render(request, 'login.html')
    
def dashboard(request):
    if not request.user.is_authenticated:
        return HttpResponse("Unauthorized", status=401)
    
    return render(request, 'dashboard.html', {'user': request.user})