from django.shortcuts import render

def login_view(request):
    return render(request, 'login.html')
    # Add your login logic here

# Add other views for your application
