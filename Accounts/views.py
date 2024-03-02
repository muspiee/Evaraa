from django.shortcuts import render

# Create your views here.

def user_auth(request):
    return render(request, 'AUTH/login_reg.html')
