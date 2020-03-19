from sys import path

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from .views import LoginView, LogoutView, Home, sondage

urlpatterns = patterns('',
                       # url(r'^$', login_required, {'template_name': 'connexion/login.html'}),
                       # url(r'^$', auth_views.login, {'template_name': 'base/index.html'}),
                       url(r'^$', auth_views.login, {'template_name': 'connexion/login.html'}),
                       # url(r'^$', Home.as_view()),
                       url(r'^login/$', LoginView.as_view()),
                       url(r'^box/$', (TemplateView.as_view(template_name='base/index.html'))),
                       url(r'^logout/$', LogoutView.as_view()),
                       # url(r'^sondage/$', Sondage.as_view()),
                       # url('upload-csv/', contact_upload, name='contact_upload'),
                       )
