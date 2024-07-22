from django.contrib.auth import (
        authenticate, 
        login, 
        logout
    )

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import (
    View,

)

from users.forms import UserRegisterForm

class LoginView(View):
    def get(self, request): # Renderiza el formulario.
        return render(
            request, 
            'home/login.html'
        
        )
    
    def post(self, request): # Información que envía el usuario.
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(
                request,
                username = username,
                password = password

            )

            if user:
                login(request, user) # Hacemos uso de la función que importamos más arriba

                return redirect('index')
        
        return redirect('login')

class LogoutView(View):
    def get(self, request):
        logout(request)
        
        return redirect('login')
    
# Create your views here.

class RegisterView(View):
    form_class = UserRegisterForm
    template_name = 'home/register.html'

    def get(self, request):
        form = self.form_class()
        return render(
            request,
            self.template_name,
            dict(
                form=form
            )
        )

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("register")
        return render(
            request,
            self.template_name,
            dict(
                form=form
            )
        )

class IndexView(View):
    def get(self, request):
        return render(
            request,
            'home/index.html'

        )