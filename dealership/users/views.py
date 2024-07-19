from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import (
    login,
    logout,
    authenticate,
)
from users.forms import UserRegisterForm

# Create your views here.

class RegisterView(View):
    form_class = UserRegisterForm
    template_name = 'register.html'

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
            # login(request, user)
            return redirect("register")
        return render(
            request,
            self.template_name,
            dict(
                form=form
            )
        )