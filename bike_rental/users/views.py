from django.contrib.auth import views as auth_views
from django.shortcuts import redirect, render
from .forms import LoginForm
from django.contrib.auth import login as auth_login


def login(request):
    form = LoginForm(request, data=request.POST or None)
    if form.is_valid():
        auth_login(request, form.get_user())
        return redirect('bike_list')
    return render(request, 'users/login.html', {'form': form})


def logout(request):
    return auth_views.LogoutView.as_view(next_page='login')(request)
