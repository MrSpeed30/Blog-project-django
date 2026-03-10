from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.clean_username.get('username')
    else:
        form = UserCreationForm()
    return render(request,'register\\register.html', {'form': form})