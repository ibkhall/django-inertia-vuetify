from django.urls import path
from . import views


urlpatterns = [
    path('login', views.login_form,name='login'),
    path('connect', views.connect,name='connect'),
]
