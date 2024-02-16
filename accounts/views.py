from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'dashboard.html')

def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            form = UserCreationForm()
    form = UserCreationForm()
    return render(request, 'registration/login.html', {'form':form})
    