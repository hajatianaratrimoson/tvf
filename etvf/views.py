from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, render, redirect
from django.http import *
from .models import *

import csv, io
from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required


class LoginView(TemplateView):
    template_name = 'front/login.html'

    def post(self, request, **kwargs):
        username = request.POST.get('username', True)
        password = request.POST.get('password', True)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL, user)
        else:
            return render(request, self.template_name)


class LogoutView(TemplateView):
    template_name = 'connexion/login.html'

    def get(self, request, **kwargs):
        logout(request)

        return render(request, self.template_name)


class Home(TemplateView):
    template_name = "connexion/login.html"
    template_name1 = "base/index.html"

    def get(self, request):
        if not request.user.is_authenticated():
            return render(request, self.template_name)
        else:
            return redirect('/box/')


class Sondage(TemplateView):
    template_name = "base/sondage.html"

    def get(self, request):
        return render(request, self.template_name)


def sondage(request):
    return render(request, 'base/sondage.html', {})
