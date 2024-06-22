from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User,Group

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            form.save()
        # adding new user
            user = User.objects.get(username=uname)
            lib_group = Group.objects.get(name='customer')
            user.groups.add(lib_group)
            user.save()
            return redirect('login')
        return redirect("index")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})