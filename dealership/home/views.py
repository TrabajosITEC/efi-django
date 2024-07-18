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

class RegisterView(View):
    form_class = UserRegisterForm
    template = 'home/register.html'

    def get(self, request):
        form = self.form_class()
        
        return render(
            request,
            self.template,
            dict(
                form = form

            )

        )
    
    """  def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('index')

        else:
            return render(
                request,
                self.template,
                dict(
                    form = form

                )

            ) """

class IndexView(View):
    def get(self, request):
        return render(
            request,
            'home/index.html'

        )