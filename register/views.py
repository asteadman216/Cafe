from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User, Group


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            uname = form.cleaned_data['username']
            user = User.objects.get(username=uname)
            lib_group = Group.objects.get(name='customer')
            user.groups.add(lib_group)
            user.save()
            return redirect('login')  # Redirect to login after successful registration
        else:
            # If form is not valid, render the registration form with errors
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})
